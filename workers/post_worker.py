import random
from datetime import datetime

from constants import constants
from logger import log


def update_database(db_connection, record_id, param):
    log("Updating db", constants.msg_info)
    db_cursor = db_connection.cursor()
    query = ''
    if param == constants.sub_category:
        query = "UPDATE submissions SET is_replied=%s, is_upvoted=%s, updated_at=%s WHERE (bot_id=%s AND submission_id=%s)"
    elif param == constants.com_category:
        query = "UPDATE comments SET is_replied=%s, is_upvoted=%s, updated_at=%s WHERE (bot_id=%s AND comment_id=%s)"

    current_data_time = datetime.now()
    date = current_data_time.strftime("%Y-%m-%d %H:%M")
    update_details = (1, 1, date, constants.bot_id, record_id)
    # try saving the data
    db_cursor.execute(query, update_details)
    db_connection.commit()
    log("Updated db", constants.msg_info)
    # close the connections
    db_cursor.close()


def send_replies_and_upvote(reddit, db_connection):
    submission_ids = get_submission_ids(db_connection, constants.sub_category)
    comment_ids = get_submission_ids(db_connection, constants.com_category)
    print(len(submission_ids))
    print(len(comment_ids))
    # get a single submission
    # handle submissions
    if len(submission_ids) > 0:
        sub_id = random.choice(submission_ids)
        submission = reddit.submission(sub_id)
        # submission.upvote()
        # submission.reply("Hello there Mumbai")
        update_database(db_connection, sub_id, "submission")

    # handle comments
    if len(comment_ids) > 0:
        comment_id = random.choice(comment_ids)
        comment = reddit.comment(comment_id)
        # comment.upvote()
        # comment.reply()
        update_database(db_connection, comment_id, "comment")


def get_submission_ids(db_connection, type_name):
    db_cursor = db_connection.cursor()
    query = ''
    if type_name == constants.sub_category:
        query = "SELECT submission_id FROM submissions WHERE is_replied=0 LIMIT 10"
    elif type_name == constants.com_category:
        query = "SELECT comment_id FROM comments WHERE is_replied=0 LIMIT 10"
    db_cursor.execute(query)
    items = db_cursor.fetchall()
    ids = []
    for row in items:
        ids.append(row[0])

    return ids
