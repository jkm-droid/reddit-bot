import os
from datetime import datetime

from dotenv import load_dotenv

from constants import constants
from logger import _logger

load_dotenv()
bot_id = os.environ.get('BOT_ID')
bot_name = os.environ.get('BOT_NAME')
bot_user_id = os.environ.get('BOT_USER_ID')


# Save the collected data to db
def save_submission_and_comment_data_to_db(db_connection, category, extracted_data):
    # save submissions/comments
    db_cursor = db_connection.cursor()
    query = ''
    target_table = ''
    if category == constants.submission_category:
        _logger().info(f"Saving submission {extracted_data['record_id']} data to db...")
        # prepare the query and data
        query = "INSERT INTO submissions (bot_id,submission_id, content,created_at) VALUES (%s,%s,%s,%s)"
        target_table = constants.submission_category

    elif category == constants.comment_category:
        _logger().info(f"Saving comment {extracted_data['record_id']} data to db...")
        # prepare the query and data
        query = "INSERT INTO comments (bot_id,comment_id, content,created_at) VALUES (%s,%s,%s,%s)"
        target_table = constants.comment_category

    # ensure no duplicates
    record_id = extracted_data['record_id']
    check = check_if_record_exists(db_cursor, bot_id, record_id, target_table)
    if check == 0:
        current_data_time = datetime.now()
        date = current_data_time.strftime("%Y-%m-%d %H:%M")
        record_details = (bot_id, record_id, extracted_data['content'], date)
        # try saving the data
        try:
            db_cursor.execute(query, record_details)
            db_connection.commit()
        except Exception as e:
            _logger().error(f"An exception occurred when saving extracted {category} {extracted_data} {e}")

        db_cursor.close()
        _logger().info(f"Saved {category} {record_id} to db")
    else:
        return


def check_if_record_exists(db_cursor, _bot_id, item_id, item_table):
    query = ''
    if item_table == constants.submission_category:
        query = "SELECT submission_id FROM submissions WHERE (bot_id=%s AND  submission_id=%s)"
    elif item_table == constants.comment_category:
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
