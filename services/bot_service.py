import logging
import os
import time
from datetime import datetime

from dotenv import load_dotenv

from constants import constants
from services import database_service

load_dotenv()

bot_id = os.environ.get('BOT_ID')
bot_name = os.environ.get('BOT_NAME')
bot_target_country = os.environ.get('BOT_TARGET_COUNTRY')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def initialize_bot(db_connection):
    # first check if bot exists
    cursor = db_connection.cursor(buffered=True, dictionary=True)
    query = "SELECT * FROM bots WHERE id=%s"
    cursor.execute(query, [bot_id])
    bot_details = cursor.fetchone()
    cursor.close()
    if bot_details is not None:
        # check the bot initialization status
        init_status = bot_details['is_initialized']
        if init_status == 0:
            # check all associated tables  data
            result = check_all_bot_tables_for_data(db_connection)
            return result
        else:
            return {
                "initialized": 1,
                "errors": []
            }
    else:
        errors = [f"Bot not found. Invalid bot id {bot_id} set up in the env"]
        save_initialization_errors_to_file(errors)
        return {
            "initialized": 0,
            "errors": errors
        }


def check_all_bot_tables_for_data(db_conn):
    keywords = database_service.count_item_in_db(db_conn, "keywords")[0]
    sub_reddits = database_service.count_item_in_db(db_conn, "sub_reddits")[0]
    errors = []
    if keywords <= 4:
        errors.append(f"insufficient keywords in db. add {5 - keywords} more keywords to proceed")

    if sub_reddits <= 4:
        errors.append(f"insufficient sub reddits in db. add {5 - sub_reddits} more sub reddit to proceed")

    if len(errors) > 0:
        save_initialization_errors_to_file(errors)
        return {
            "initialized": 0,
            "errors": errors
        }
    else:
        cursor = db_conn.cursor()
        query = "UPDATE bots SET is_initialized=%s WHERE id=%s"
        cursor.execute(query, (1, bot_id))
        db_conn.commit()
        cursor.close()

        return {
            "initialized": 1,
            "errors": errors
        }


def save_initialization_errors_to_file(errors):
    current_data_time = datetime.now()
    date = current_data_time.strftime("%Y-%m-%d %H:%M")
    with open(f"{bot_name.replace('-', '_')}_initialization_errors", 'a', encoding="utf-8") as f:
        f.write(f"{bot_name} initialization errors on {date} \n")
        for error in errors:
            f.write(f"ERROR: {error}\n")
            f.write("\n")
        f.close()
