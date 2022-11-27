import time

from workers import post_worker, reddit_worker, database_worker
from configs.config import create_reddit
from configs.database import create_db_connection
from logger import log
from constants import constants


def main():
    log("connecting...please wait", constants.msg_info)

    # establish connection to reddit
    reddit = create_reddit()
    if reddit:
        log(f"connected as {reddit.user.me()}", constants.msg_info)
        while True:
            try:
                # establish db connection
                db_connection = create_db_connection()
                count = database_worker.count_db_records(db_connection)
                log(f"Current records: {count}", constants.msg_info)
                if count == 0:
                    log("inside reddit worker", constants.msg_info)
                    # extract submission and comment ids
                    # save the ids in a text file
                    reddit_worker.extract_data_from_reddit(reddit, "SpaceJam2021", "poland")

                    # read data from text file and insert/update db
                    database_worker.save_data_to_db(db_connection)

                    # remove files
                    reddit_worker.delete_data_files()
                else:
                    log("inside post worker", constants.msg_info)
                    # get data from db and start sending replies
                    post_worker.send_replies_and_upvote(reddit, db_connection)

                log("Sleeping in main", constants.msg_info)
                log("\n", constants.msg_info)
                time.sleep(50)
            except Exception as e:
                log(f"An exception occurred {e}", constants.msg_info)
                time.sleep(100)
    else:
        log("Connection could not be established", constants.msg_error)


if __name__ == "__main__":
    main()
