import time

from services import post_service, reddit_service, database_service, sub_reddit_service, keyword_service
from configs.config import create_reddit
from configs.database import create_db_connection
from logger import log
from constants import constants


def main():
    log("connecting...please wait", constants.msg_info)

    # establish connection to reddit
    reddit = True # create_reddit()
    if reddit:
        # log(f"connected as {reddit.user.me()}", constants.msg_info)
        while True:
            try:
                # establish db connection
                db_connection = create_db_connection()
                count = database_service.count_db_records(db_connection)
                log(f"Current records: {count}", constants.msg_info)
                if count == 0:
                    log("inside reddit worker", constants.msg_info)
                    # get sub_reddit and keyword
                    sub_reddit_details = sub_reddit_service.sub_reddit(db_connection)
                    sub_reddit_id = sub_reddit_details["sub_reddit_id"]
                    sub_reddit_name = sub_reddit_details["sub_reddit_name"]
                    log(f"Sub reddit : {sub_reddit_details}", constants.msg_info)
                    # get keyword
                    keyword_name = keyword_service.keyword(db_connection, sub_reddit_id)
                    log(f"Keyword : {keyword_name}", constants.msg_info)

                    # extract submission and comment ids
                    # save the ids in a text file
                    reddit_service.extract_data_from_reddit(reddit, sub_reddit_name, keyword_name)

                    # read data from text file and insert/update db
                    database_service.save_data_to_db(db_connection)

                    # remove files
                    reddit_service.delete_data_files()
                else:
                    log("inside post worker", constants.msg_info)
                    # get data from db and start sending replies
                    # post_service.send_replies_and_upvote(reddit, db_connection)

                log("Sleeping in main", constants.msg_info)
                log("\n", constants.msg_info)
                time.sleep(50)
            except Exception as e:
                log(f"An exception occurred {e}", constants.msg_error)
                time.sleep(100)
    else:
        log("Connection could not be established", constants.msg_error)


if __name__ == "__main__":
    main()
