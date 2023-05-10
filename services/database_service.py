import os
from datetime import datetime
from constants import constants
from logger import log
from dotenv import load_dotenv

load_dotenv()
bot_id = os.environ.get('BOT_ID')
bot_name = os.environ.get('BOT_NAME')
bot_user_id = os.environ.get('BOT_USER_ID')


# Save the collected data to db
def save_submission_data_to_db(db_connection):
    # save submissions
    save_records(db_connection, constants.submission_category)
    db_connection.close()
    log("Saved submissions data to db", constants.msg_info)


# Save the collected data to db
def save_comment_data_to_db(db_connection):
    # save comments
    save_records(db_connection, constants.comment_category)
    db_connection.close()
    log("Saved comments data to db", constants.msg_info)


def save_records(db_connection, category):
    db_cursor = db_connection.cursor()
    record_ids = []
    query = ''
    target_table = ''
    if category == constants.submission_category and os.path.isfile(constants.submission_file):
        log("Saving submissions data to db", constants.msg_info)
        submission_file = open(constants.submission_file, 'r').read().splitlines()
        record_ids = list(submission_file)
        # prepare the query and data
        query = "INSERT INTO submissions (bot_id,submission_id,created_at) VALUES (%s,%s,%s)"
        target_table = constants.submission_category

    elif category == constants.comment_category and os.path.isfile(constants.comment_file):
        log("Saving comments data to db", constants.msg_info)
        comment_file = open(constants.comment_file, 'r').read().splitlines()
        record_ids = list(comment_file)
        # prepare the query and data
        query = "INSERT INTO comments (bot_id,comment_id,created_at) VALUES (%s,%s,%s)"
        target_table = constants.comment_category

    for record_id in record_ids:
        # ensure no duplicates
        check = check_if_record_exists(db_cursor, bot_id, record_id, target_table)
        if check == 0:
            current_data_time = datetime.now()
            date = current_data_time.strftime("%Y-%m-%d %H:%M")
            record_details = (bot_id, record_id, date)
            # try saving the data
            db_cursor.execute(query, record_details)
            db_connection.commit()

    db_cursor.close()


def check_if_record_exists(db_cursor, _bot_id, item_id, item_type):
    query = ''
    if item_type == constants.submission_category:
        query = "SELECT submission_id FROM submissions WHERE (bot_id=%s AND  submission_id=%s)"
    elif item_type == constants.comment_category:
        query = "SELECT comment_id FROM comments WHERE (bot_id=%s AND  comment_id=%s)"

    db_cursor.execute(query, (_bot_id, item_id))
    item = db_cursor.fetchone()
    if item is not None:
        return 1
    else:
        return 0


def count_db_records(db_connection):
    db_cursor = db_connection.cursor()
    submission_query = "SELECT COUNT(*) FROM submissions WHERE (is_replied=%s AND  is_upvoted=%s)"
    comment_query = "SELECT COUNT(*) FROM comments WHERE (is_replied=%s AND  is_upvoted=%s)"
    db_cursor.execute(submission_query, (0, 0))
    result = db_cursor.fetchone()
    sub_count = result[0]

    db_cursor.execute(comment_query, (0, 0))
    result = db_cursor.fetchone()
    com_count = result[0]
    db_cursor.close()

    return sub_count + com_count
