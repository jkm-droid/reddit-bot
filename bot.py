import time

import pyfiglet

from configs.database import create_db_connection
from configs.reddit import create_reddit
from logger import _logger
from services import reddit_service, database_service, sub_reddit_service, keyword_service, bot_service, post_service


def main():
    ascii_banner = pyfiglet.figlet_format("Reddit Bot")
    print(ascii_banner)
    _logger().info("connecting to reddit api...")

    # establish connection to reddit
    reddit = create_reddit()
    if reddit:
        _logger().info(f"connected as {reddit.user.me()}")
        while True:
            try:
                bot_should_sleep = True
                # establish db connection
                _logger().info("connecting to db...")
                db_connection = create_db_connection()
                _logger().info("Initializing bot...")
                result = bot_service.initialize_bot(db_connection)
                init_msg = result['initialized']
                if init_msg == 0:
                    _logger().info(
                        "Some errors occurred when initializing bot. See more details in the error _logger().infos file")
                    break
                elif init_msg == 1:
                    _logger().info("Initialized bot successfully")
                    count = database_service.count_db_records(db_connection)
                    _logger().info(f"Current records: {count}")
                    if count == 0:
                        # get sub_reddit and keyword
                        sub_reddit_details = sub_reddit_service.sub_reddit(db_connection)
                        sub_reddit_id = sub_reddit_details["sub_reddit_id"]
                        sub_reddit_name = sub_reddit_details["sub_reddit_name"]
                        _logger().info(f"Sub reddit : {sub_reddit_name}")

                        # get keyword
                        keyword_result = keyword_service.keyword(db_connection, sub_reddit_id)
                        keyword_name = keyword_result['keyword_name']
                        if keyword_result['set_to_default'] == 1:
                            sub_reddit_name = keyword_result['sub_reddit_name']
                            _logger().info(f"Sub reddit after resetting to default : {sub_reddit_name}")

                        _logger().info(f"Keyword : {keyword_name}")

                        # extract submission and comment ids
                        # save the ids in the db
                        reddit_service.extract_data_from_reddit(reddit, db_connection, sub_reddit_name, keyword_name)
                        db_connection.close()
                        _logger().info(f"Sleeping after extracting a single key word {keyword_name}")
                        time.sleep(300)
                        bot_should_sleep = False
                    else:
                        _logger().info("Inside post worker")
                        # get data from db and start sending replies
                        post_service.send_replies_and_upvote(reddit, db_connection)
                        db_connection.close()
                    if bot_should_sleep:
                        _logger().info("Sleeping in main")
                        _logger().info("\n")
                        time.sleep(600)  # 10 mins
                else:
                    _logger().error("An error occurred when initializing bot")
            except Exception as e:
                _logger().error(f"An exception occurred {e}", exc_info=True)
                time.sleep(300)  # 5 mins
    else:
        _logger().error("Connection could not be established")


if __name__ == "__main__":
    main()
