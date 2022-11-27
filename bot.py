from workers import post_worker
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
        # # extract submission and comment ids
        # # save the ids in a text file
        # reddit_worker.extract_data_from_reddit(reddit, "SpaceJam2021", "visiting")
        #
        # # establish db connection
        # # read data from text file and insert/update db
        db_connection = create_db_connection()
        # database_worker.save_data_to_db(db_connection)
        #
        # # remove files
        # reddit_worker.delete_data_files()

        # get data from db and start sending replies
        post_worker.send_replies_and_upvote(reddit, db_connection)
    else:
        log("Connection could not be established", constants.msg_error)


if __name__ == "__main__":
    main()
