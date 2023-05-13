import os
import time

from configs.config import create_reddit
from configs.database import create_db_connection
from constants import constants
from logger import log
from services import reddit_service, database_service, sub_reddit_service, keyword_service, bot_service, post_service

bot_should_sleep = True


def main():
    global bot_should_sleep
    log("connecting to api...please wait", constants.msg_info)

    # establish connection to reddit
    reddit = create_reddit()
    if reddit:
        log(f"connected as {reddit.user.me()}", constants.msg_info)
        while True:
            try:
                # establish db connection
                log("connecting to db...", constants.msg_info)
                db_connection = create_db_connection()
                log("initializing bot...", constants.msg_info)
                result = bot_service.initialize_bot(db_connection)
                init_msg = result['initialized']
                if init_msg == 0:
                    log("Some errors occurred when initializing bot. See more details in the error logs file",
                        constants.msg_error)
                    break
                elif init_msg == 1:
                    log("initialized bot successfully", constants.msg_info)
                    count = database_service.count_db_records(db_connection)
                    log(f"Current records: {count}", constants.msg_info)
                    if count == 0:
                        # get sub_reddit and keyword
                        sub_reddit_details = sub_reddit_service.sub_reddit(db_connection)
                        sub_reddit_id = sub_reddit_details["sub_reddit_id"]
                        sub_reddit_name = sub_reddit_details["sub_reddit_name"]
                        log(f"Sub reddit : {sub_reddit_name}", constants.msg_info)

                        # get keyword
                        keyword_result = keyword_service.keyword(db_connection, sub_reddit_id)
                        keyword_name = keyword_result['keyword_name']
                        if keyword_result['set_to_default'] == 1:
                            sub_reddit_name = keyword_result['sub_reddit_name']
                            log(f"Sub reddit after resetting to default : {sub_reddit_name}", constants.msg_info)

                        log(f"Keyword : {keyword_name}", constants.msg_info)

                        # extract submission and comment ids
                        # save the ids in the db
                        reddit_service.extract_data_from_reddit(reddit, db_connection, sub_reddit_name, keyword_name)
                        bot_should_sleep = False
                    else:
                        log("inside post worker", constants.msg_info)
                        # get data from db and start sending replies
                        post_service.send_replies_and_upvote(reddit, db_connection)

                    if bot_should_sleep:
                        log("Sleeping in main", constants.msg_info)
                        log("\n", constants.msg_info)
                        time.sleep(60)
                else:
                    log("An error occurred when initializing bot", constants.msg_error)
            except Exception as e:
                log(f"An exception occurred {e}", constants.msg_error)
                time.sleep(100)
    else:
        log("Connection could not be established", constants.msg_error)


if __name__ == "__main__":
    main()
