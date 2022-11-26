from config import create_reddit
from database import create_db_connection
from logger import log
import constants
import reddit_worker


def main():
    log("connecting...please wait", constants.msg_info)

    # establish connection to reddit
    reddit = create_reddit()
    if reddit:
        log(f"connected as {reddit.user.me()}", constants.msg_info)
        # extract submission and comment ids
        # save the ids in a text file
        reddit_worker.extract_data_from_reddit(reddit, "Minecraft", "build")

        # establish db connection
        # read data from text file and insert/update db
        # close db
        db_connection = create_db_connection()
        reddit_worker.save_data_to_db(db_connection)
        db_connection.close()
    else:
        log("Connection could not be established", constants.msg_error)


if __name__ == "__main__":
    main()
