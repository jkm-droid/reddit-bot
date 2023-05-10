import os
import random
from datetime import datetime
from dotenv import load_dotenv
from constants import constants
from logger import log

load_dotenv()
bot_id = os.environ.get('BOT_ID')


def count_item(db_connection, category_table):
    db_cursor = db_connection.cursor(buffered=True)
    query = f"SELECT COUNT(*) FROM {category_table} WHERE is_replied=%s"
    db_cursor.execute(query, [0])
    result = db_cursor.fetchone()
    count = result[0]
    db_cursor.close()

    return count


def send_replies_and_upvote(reddit, db_connection):
    sub_count = count_item(db_connection, constants.submission_category)
    if sub_count > 0:
        submission_ids = get_submission_ids(db_connection, constants.submission_category)
        print(len(submission_ids))
        # get a single submission
        # handle submissions
        if len(submission_ids) > 0:
            sub_id = random.choice(submission_ids)
            submission = reddit.submission(sub_id)
            # submission.upvote()
            submission_reply = get_reddit_reply_from_db(db_connection)
            # submission.reply(submission_reply)
            update_submission_or_comment(db_connection, sub_id, "submission")
    else:
        log("All submissions in db have been replied", constants.msg_info)

    com_count = count_item(db_connection, constants.comment_category)
    if com_count > 0:
        comment_ids = get_submission_ids(db_connection, constants.comment_category)
        print(len(comment_ids))
        # handle comments
        if len(comment_ids) > 0:
            comment_id = random.choice(comment_ids)
            comment = reddit.comment(comment_id)
            # comment.upvote()
            comment_reply = get_reddit_reply_from_db(db_connection)
            # comment.reply(comment_reply)
            update_submission_or_comment(db_connection, comment_id, "comment")
    else:
        log("All comments in db have been replied", constants.msg_info)


def update_submission_or_comment(db_connection, record_id, param):
    log("Updating db", constants.msg_info)
    db_cursor = db_connection.cursor()
    query = ''
    if param == constants.submission_category:
        query = "UPDATE submissions SET is_replied=%s, is_upvoted=%s, updated_at=%s WHERE (bot_id=%s AND submission_id=%s)"
    elif param == constants.comment_category:
        query = "UPDATE comments SET is_replied=%s, is_upvoted=%s, updated_at=%s WHERE (bot_id=%s AND comment_id=%s)"

    current_data_time = datetime.now()
    date = current_data_time.strftime("%Y-%m-%d %H:%M")
    update_details = (1, 1, date, bot_id, record_id)
    # try updating the data
    db_cursor.execute(query, update_details)
    db_connection.commit()
    log("Updated db", constants.msg_info)
    # close the connections
    db_cursor.close()


def get_submission_ids(db_connection, type_name):
    db_cursor = db_connection.cursor(buffered=True, dictionary=True)
    query = ''
    if type_name == constants.submission_category:
        query = "SELECT submission_id FROM submissions WHERE is_replied=%s LIMIT 10"
    elif type_name == constants.comment_category:
        query = "SELECT comment_id FROM comments WHERE is_replied=%s LIMIT 10"
    db_cursor.execute(query, [0])
    items = db_cursor.fetchall()
    ids = []
    for row in items:
        ids.append(row['id'])

    return ids


def get_reddit_reply_from_db(db_connection):
    record = get_item(db_connection)
    if record is not None:
        # set selected reply
        update_item(db_connection, record['id'])

        return record['description']
    else:
        # update all reddit replies status to 0
        try:
            update_cursor = db_connection.cursor(buffered=True)
            update_all_query = "UPDATE reddit_replies SET is_replied=%s WHERE bot_id=%s"
            update_cursor.execute(update_all_query, [0, bot_id])
            db_connection.commit()
            update_cursor.close()
        except Exception as e:
            log(f"An exception occurred updating all reddit replies for bot {bot_id} {e}", constants.msg_error)
            # Rolling back in case of error
            db_connection.rollback()

        record = get_item(db_connection)
        update_item(db_connection, record['id'])

        return record['description']


def get_item(db_connection):
    db_cursor = db_connection.cursor(buffered=True, dictionary=True)
    query = "SELECT id,description FROM reddit_replies WHERE (is_replied=%s AND bot_id=%s) LIMIT 1"
    db_cursor.execute(query, [0, bot_id])
    record = db_cursor.fetchone()
    db_cursor.close()

    return record


def update_item(db_connection, item_id):
    db_cursor = db_connection.cursor(buffered=True)
    try:
        update_query = "UPDATE reddit_replies SET is_replied=%s WHERE id=%s"
        db_cursor.execute(update_query, (1, item_id))
        db_connection.commit()
        db_cursor.close()
    except Exception as e:
        log(f"An exception occurred updating reddit reply {e}", constants.msg_error)
        # Rolling back in case of error
        db_connection.rollback()
