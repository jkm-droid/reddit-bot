import os
from dotenv import load_dotenv
from logger import log
from constants import constants

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
        log(f"sub reddit name {sub_reddit_details['sub_reddit_name']}", constants.msg_info)

        return sub_reddit_details
    else:
        lock_subreddit(db_connection)

        sub_reddit_details = get_locked_subreddit_from_db(db_connection)
        log(f"sub reddit name {sub_reddit_details['sub_reddit_name']}", constants.msg_info)

        return sub_reddit_details


# get one subreddit and set it to locked status.
# Extract data from the sub_reddit by looping all
# through the keywords and setting extracted status to true once extracted
def get_locked_subreddit_from_db(db_connection):
    db_cursor = db_connection.cursor(buffered=True)
    sub_reddit_query = "SELECT * FROM sub_reddits WHERE (bot_id=%s AND is_extracted=%s AND  is_locked=%s)"
    db_cursor.execute(sub_reddit_query, (bot_id, 0, 1))
    response = db_cursor.fetchone()
    sub_id = response[0]
    name = response[2]
    is_extracted = response[3]
    is_locked = response[6]
    db_cursor.close()

    return {
        "sub_reddit_id": sub_id,
        "sub_reddit_name": name,
        "is_extracted": is_extracted,
        "is_locked": is_locked,
    }


def lock_subreddit(db_connection):
    db_cursor = db_connection.cursor(buffered=True)
    sub_reddit_query = "SELECT * FROM sub_reddits WHERE (bot_id=%s AND is_extracted=%s)"
    db_cursor.execute(sub_reddit_query, (bot_id, 0))
    result = db_cursor.fetchone()
    if result is not None:
        sub_reddit_id = result[0]
        db_cursor.close()
        update_sub_reddit_query = "UPDATE sub_reddits SET is_locked=%s WHERE id=%s"
        record_details = (1, sub_reddit_id)
        # try updating the record
        try:
            update_cursor = db_connection.cursor(buffered=True)
            update_cursor.execute(update_sub_reddit_query, record_details)
            db_connection.commit()
            update_cursor.close()
        except Exception as e:
            log(f"An exception occurred {e}", constants.msg_error)
            # Rolling back in case of error
            db_connection.rollback()


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
