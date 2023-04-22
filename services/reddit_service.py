import os
import re
from constants import constants
from logger import log


# This section calls the other functions responsible for
# extracting the data from reddit
def extract_data_from_reddit(reddit, sub_name, keyword):
    log("extracting data...please wait", constants.msg_info)

    # check keyword across subreddit's top submissions
    log(f"[{constants.sub_top}] submission", constants.msg_info)
    check_keyword_from_submissions(reddit, sub_name, keyword, "top")

    # check keyword across subreddit's hot submissions
    log(f"[{constants.sub_hot}] submission", constants.msg_info)
    check_keyword_from_submissions(reddit, sub_name, keyword, "hot")

    # check keyword across subreddit's comments
    log(f"checking comment", constants.msg_info)
    for comment in reddit.subreddit(sub_name).comments(limit=1000):
        check_keyword_from_comments(comment, keyword)


# Save extracted ids to a text file
def save_data_to_file(filename, data):
    with open(f"{filename}.txt", 'a') as data_file:
        data_file.write(data)
        data_file.write("\n")


# This section deals with reddit submissions from a particular subreddit
def check_keyword_from_submissions(reddit, sub_name, keyword, sub_category):
    if sub_category == "hot":
        submissions = reddit.subreddit(sub_name).hot()
    elif sub_category == "top":
        submissions = reddit.subreddit(sub_name).top()
    else:
        submissions = reddit.subreddit(sub_name).new()

    for submission in submissions:
        # check if the keyword is present in submission
        if re.search(keyword, submission.title, re.IGNORECASE):
            # save the found submissions ids in text file
            if not os.path.isfile(constants.submission_file):
                save_data_to_file("submissions", submission.id)

            # ensure there are no duplicates
            submission_ids = open(constants.submission_file, 'r', encoding='utf-8')
            ids = submission_ids.read()

            if re.search(submission.id, ids):
                submission_ids.close()
            else:
                save_data_to_file("submissions", submission.id)


# This section deals with reddit comments from a particular subreddit
def check_keyword_from_comments(comment, keyword):
    if re.search(keyword, comment.body, re.IGNORECASE):
        # save the found comment ids in text file
        if not os.path.isfile(constants.comment_file):
            save_data_to_file("comments", comment.id)

        # ensure the ids are not in the file - avoid duplicates
        comment_file = open(constants.comment_file, 'r', encoding='utf-8')
        ids = comment_file.read()

        if re.search(comment.id, ids):
            comment_file.close()
        else:
            save_data_to_file("comments", comment.id)


# delete text files from the system
def delete_data_files():
    log("Removing data files", constants.msg_info)
    os.remove(constants.submission_file)
    os.remove(constants.comment_file)
    log("Removed data files", constants.msg_info)
