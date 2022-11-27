import os
from datetime import datetime

from constants import constants
from logger import log


# Save the collected data to db
def save_data_to_db(db_connection):
    # save submissions
    save_records(db_connection, constants.sub_category)
    # save comments
    save_records(db_connection, constants.com_category)
    db_connection.close()
    log("Saved data to db", constants.msg_info)


def save_records(db_connection, category):
    db_cursor = db_connection.cursor()
    record_ids = []
    query = ''
    if os.path.isfile(constants.submission_file) or os.path.isfile(constants.comment_file):
        if category == constants.sub_category and os.path.isfile(constants.submission_file):
            log("Saving submissions data to db", constants.msg_info)
            submission_file = open(constants.submission_file, 'r').read().splitlines()
            record_ids = list(submission_file)
            # prepare the query and data
            query = "INSERT INTO submissions (bot_id,submission_id,created_at) VALUES (%s,%s,%s)"

        elif category == constants.com_category and os.path.isfile(constants.comment_file):
            log("Saving comments data to db", constants.msg_info)
            comment_file = open(constants.comment_file, 'r').read().splitlines()
            record_ids = list(comment_file)
            # prepare the query and data
            query = "INSERT INTO comments (bot_id,comment_id,created_at) VALUES (%s,%s,%s)"

        for record_id in record_ids:
            # ensure no duplicates
            check = check_if_record_exists(db_cursor, constants.bot_id, record_id, "submission")
            if check == 0:
                current_data_time = datetime.now()
                date = current_data_time.strftime("%Y-%m-%d %H:%M")
                record_details = (constants.bot_id, record_id, date)
                # try saving the data
                db_cursor.execute(query, record_details)
                db_connection.commit()

        # close the connections
        db_cursor.close()
    else:
        log("No data files were found", constants.msg_info)


def check_if_record_exists(db_cursor, bot_id, item_id, item_type):
    query = ''
    if item_type == constants.sub_category:
        query = "SELECT submission_id FROM submissions WHERE (bot_id=%s AND  submission_id=%s)"
    elif item_type == constants.com_category:
        query = "SELECT comment_id FROM comments WHERE (bot_id=%s AND  comment_id=%s)"

    db_cursor.execute(query, (bot_id, item_id))
    item = db_cursor.fetchone()
    if item:
        return 1
    else:
        return 0
