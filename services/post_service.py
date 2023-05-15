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


def update_submission_or_comment_with_exception_data(db_connection, item_id, item_table, e):
    try:
        db_cursor = db_connection.cursor(buffered=True)
        update_query = f"UPDATE {item_table} SET processing_status=%s, response_description=%s,updated_at=%s WHERE {item_id} "
        current_data_time = datetime.now()
        date = current_data_time.strftime("%Y-%m-%d %H:%M")
        db_cursor.execute(update_query, ('FAILED', e, date))
        db_connection.commit()
        db_cursor.close()
    except Exception as e:
        log(f'Failed updating {item_table} with exception data. Exception {e}', constants.msg_error)
        db_connection.rollback()


def send_replies_and_upvote(reddit, db_connection):
    sub_count = count_item(db_connection, constants.submission_table)
    if sub_count > 0:
        submission_id = get_submission_or_comment_ids(db_connection, constants.submission_category)
        submission_reply = get_reddit_reply_from_db(db_connection)
        # get a single submission
        # handle submission upvote and reply
        if submission_id is not None:
            sub_id = f'submission_id={submission_id}'
            try:
                submission = reddit.submission(submission_id)
                submission.upvote()
                submission.reply(submission_reply)
                update_submission_or_comment(db_connection, sub_id, constants.submission_table)
                log(f"Upvoted and replied to {constants.submission_category} {submission_id}", constants.msg_info)
            except Exception as e:
                # TODO handle submissions that were not replied/up voted
                update_submission_or_comment_with_exception_data(db_connection, sub_id,
                                                                 constants.submission_table, e)
                log(f"An exception occurred when up voting/replying to submission {submission_id} : {e}",
                    constants.msg_error)

    else:
        log("All submissions in db have been replied", constants.msg_info)

    com_count = count_item(db_connection, constants.comment_table)
    if com_count > 0:
        comment_id = get_submission_or_comment_ids(db_connection, constants.comment_category)
        comment_reply = get_reddit_reply_from_db(db_connection)
        # handle comments upvote and reply
        if comment_id is not None:
            com_id = f'comment_id={comment_id}'
            try:
                comment = reddit.comment(comment_id)
                comment.upvote()
                comment.reply(comment_reply)
                update_submission_or_comment(db_connection, com_id, constants.comment_table)
                log(f"Upvoted and replied to {constants.comment_category} {comment_id}", constants.msg_info)
            except Exception as e:
                # TODO handle comments that were not replied/up voted
                update_submission_or_comment_with_exception_data(db_connection, com_id, constants.comment_table, e)
                log(f"An exception occurred when up voting/replying to comment {comment_id} : {e}", constants.msg_error)
    else:
        log("All comments in db have been replied", constants.msg_info)


def update_submission_or_comment(db_connection, item_id, item_table):
    log(f"Updating {item_table}", constants.msg_info)
    db_cursor = db_connection.cursor()
    query = f"UPDATE {item_table} SET is_replied=%s, is_upvoted=%s,processing_status=%s,response_description=%s,updated_at=%s WHERE (bot_id=%s AND {item_id})"

    current_data_time = datetime.now()
    date = current_data_time.strftime("%Y-%m-%d %H:%M")
    update_details = (1, 1, 'SUCCESS', 'Processed', date, bot_id)
    # try updating the data
    db_cursor.execute(query, update_details)
    db_connection.commit()
    log(f"Updated {item_table}", constants.msg_info)
    # close the connections
    db_cursor.close()


def get_submission_or_comment_ids(db_connection, type_name):
    db_cursor = db_connection.cursor(buffered=True, dictionary=True)
    query = ''
    type_id = ''
    if type_name == constants.submission_category:
        query = "SELECT submission_id FROM submissions WHERE is_replied=%s LIMIT 10"
        type_id = 'submission_id'
    elif type_name == constants.comment_category:
        query = "SELECT comment_id FROM comments WHERE is_replied=%s LIMIT 10"
        type_id = 'comment_id'
    db_cursor.execute(query, [0])
    item = db_cursor.fetchone()

    return item[type_id]


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
