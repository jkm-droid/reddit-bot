import re
import os
from datetime import datetime

from logger import log
import constants


# Save the collected data to db
def save_data_to_db(db_connection):
    # save submissions
    save_submissions(db_connection)
    # save comments
    save_comments(db_connection)

    log("Saved data to db", constants.msg_info)


def save_submissions(db_connection):
    db_cursor = db_connection.cursor()
    submission_file = open(constants.submission_file, 'r').read().splitlines()
    submission_ids = list(submission_file)

    log("Saving submissions data to db", constants.msg_info)
    for submission_id in submission_ids:
        # ensure no duplicates
        check = check_if_record_exists(db_cursor, constants.bot_id, submission_id, "submission")
        if check == 0:
            current_data_time = datetime.now()
            date = current_data_time.strftime("%Y-%m-%d %H:%M")
            # prepare the query and data
            query = "INSERT INTO submissions (bot_id,submission_id,created_at) VALUES (%s,%s,%s)"
            submission_details = (constants.bot_id, submission_id, date)
            # try saving the data
            db_cursor.execute(query, submission_details)
            db_connection.commit()

    # close the connections
    db_cursor.close()


def check_if_record_exists(db_cursor, bot_id, item_id, item_type):
    query = ''
    if item_type == "submission":
        query = "SELECT submission_id FROM submissions WHERE (bot_id=%s AND  submission_id=%s)"
    elif item_type == "comment":
        query = "SELECT comment_id FROM comments WHERE (bot_id=%s AND  comment_id=%s)"

    db_cursor.execute(query, (bot_id, item_id))
    item = db_cursor.fetchone()
    if item:
        return 1
    else:
        return 0


def save_comments(db_connection):
    db_cursor = db_connection.cursor()
    comment_file = open(constants.comment_file, 'r').read().splitlines()
    comment_ids = list(comment_file)

    log("Saving comments data to db", constants.msg_info)
    for comment_id in comment_ids:
        # ensure no duplicates
        check = check_if_record_exists(db_cursor, constants.bot_id, comment_id, "comment")
        if check == 0:
            current_data_time = datetime.now()
            date = current_data_time.strftime("%Y-%m-%d %H:%M")
            # prepare the query and data
            query = "INSERT INTO comments (bot_id,comment_id,created_at) VALUES (%s,%s,%s)"
            comment_details = (constants.bot_id, comment_id, date)
            # try saving the data
            db_cursor.execute(query, comment_details)
            db_connection.commit()

    # close the connections
    db_cursor.close()