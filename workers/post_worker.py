from constants import constants


def send_replies_and_upvote(reddit, db_connection):
    submission_ids = get_submission_ids(db_connection, constants.sub_category)
    comment_ids = get_submission_ids(db_connection, constants.com_category)
    for sub_id in submission_ids:
        if sub_id == "tioh1a":
            submission = reddit.submission(sub_id)
            submission.reply("Hello there Mumbai")


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
