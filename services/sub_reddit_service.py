import os

from dotenv import load_dotenv

from logger import _logger

load_dotenv()
bot_id = os.environ.get('BOT_ID')
bot_name = os.environ.get('BOT_NAME')
bot_user_id = os.environ.get('BOT_USER_ID')


# check if the db has a locked record
# if record exists - get the record
# else lock a new record
def sub_reddit(db_connection):
    check = check_if_locked_sub_reddit_exists(db_connection, bot_id)

    if check == 1:
        sub_reddit_details = get_locked_subreddit_from_db(db_connection)

        return sub_reddit_details
    else:
        result = get_un_extracted_sub_reddit(db_connection)
        if result is not None:
            lock_subreddit(db_connection, result['id'])
        else:
            cursor = db_connection.cursor(buffered=True)
            update_subreddit_query = "UPDATE sub_reddits SET is_extracted=%s WHERE bot_id=%s"
            details = (0, bot_id)
            cursor.execute(update_subreddit_query, details)
            db_connection.commit()

            result = get_un_extracted_sub_reddit(db_connection)

            lock_subreddit(db_connection, result[0])

        sub_reddit_details = get_locked_subreddit_from_db(db_connection)

        return sub_reddit_details


def lock_subreddit(db_connection, sub_reddit_id):
    update_sub_reddit_query = "UPDATE sub_reddits SET is_locked=%s WHERE id=%s"
    record_details = (1, sub_reddit_id)
    # try updating the record
    try:
        update_cursor = db_connection.cursor(buffered=True)
        update_cursor.execute(update_sub_reddit_query, record_details)
        db_connection.commit()
        update_cursor.close()
    except Exception as e:
        _logger().error(f"An exception occurred {e}", exc_info=True)
        # Rolling back in case of error
        db_connection.rollback()


# get one subreddit and set it to locked status.
# Extract data from the sub_reddit by looping all
# through the keywords and setting extracted status to true once extracted
def get_locked_subreddit_from_db(db_connection):
    db_cursor = db_connection.cursor(buffered=True, dictionary=True)
    sub_reddit_query = "SELECT * FROM sub_reddits WHERE (bot_id=%s AND is_extracted=%s AND  is_locked=%s)"
    db_cursor.execute(sub_reddit_query, (bot_id, 0, 1))
    response = db_cursor.fetchone()
    sub_id = response['id']
    name = response['name']
    is_extracted = response['is_extracted']
    is_locked = response['is_locked']
    db_cursor.close()

    return {
        "sub_reddit_id": sub_id,
        "sub_reddit_name": name,
        "is_extracted": is_extracted,
        "is_locked": is_locked,
    }


def check_if_locked_sub_reddit_exists(db_connection, _bot_id):
    db_cursor = db_connection.cursor(buffered=True)
    check_locked_status_query = "SELECT COUNT(*) FROM sub_reddits WHERE (bot_id=%s AND  is_locked=%s)"
    db_cursor.execute(check_locked_status_query, (_bot_id, 1))
    item = db_cursor.fetchone()
    db_cursor.close()
    if item[0] <= 0:
        return 0
    else:
        return 1


def get_un_extracted_sub_reddit(db_connection):
    db_cursor = db_connection.cursor(buffered=True, dictionary=True)
    sub_reddit_query = "SELECT * FROM sub_reddits WHERE (bot_id=%s AND is_extracted=%s)"
    db_cursor.execute(sub_reddit_query, (bot_id, 0))

    return db_cursor.fetchone()
