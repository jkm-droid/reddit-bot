import os

from dotenv import load_dotenv

import constants.constants
from logger import log
from constants import constants

load_dotenv()
bot_id = os.environ.get('BOT_ID')
bot_name = os.environ.get('BOT_NAME')
bot_user_id = os.environ.get('BOT_USER_ID')


def keyword(db_connection, sub_reddit_id):
    keyword_result = get_keyword_from_db(db_connection)
    if keyword_result is not None:
        db_cursor = db_connection.cursor(buffered=True)
        # mark keyword as extracted
        update_query = "UPDATE keywords SET is_extracted=%s WHERE id=%s"
        db_cursor.execute(update_query, (1, keyword_result[0]))
        db_connection.commit()

        # return keyword name
        return keyword_result[2]
    else:
        update_sub_reddit_and_keywords(db_connection, sub_reddit_id)

        return get_keyword_from_db(db_connection)


def get_keyword_from_db(db_connection):
    db_cursor = db_connection.cursor(buffered=True)
    keyword_query = "SELECT * FROM keywords WHERE (bot_id=%s AND is_extracted=%s)"
    db_cursor.execute(keyword_query, (bot_id, 0))
    result = db_cursor.fetchone()
    # db_cursor.close()

    return result


def update_sub_reddit_and_keywords(db_connection, sub_reddit_id):
    try:
        db_cursor = db_connection.cursor(buffered=True)
        # update all keywords for this bot to false
        update_query = "UPDATE keywords SET is_extracted=%s WHERE bot_id=%s"
        db_cursor.execute(update_query, (0, bot_id))

        update_subreddit_query = "UPDATE sub_reddits SET is_extracted=%s, is_locked=%s WHERE id=%s"
        db_cursor.execute(update_subreddit_query, (1, 0, sub_reddit_id))
        db_connection.commit()
        db_cursor.close()
    except Exception as e:
        log(f"Failed updating sub_reddit and keyword with error : {e}", constants.msg_error)
