from config import create_reddit
from logger import log
import constants
import worker


def main():
    log("connecting...please wait", constants.msg_info)

    # establish connection to reddit
    reddit = create_reddit()
    if reddit:
        log("connected", constants.msg_info)
        log(reddit.user.me(), constants.msg_info)

        worker.get_keywords_from_reddit(reddit, "Minecraft", "game")
    else:
        log("Connection could not be established", constants.msg_error)


if __name__ == "__main__":
    main()
