import os
import re
from constants import constants
from logger import log
from services.database_service import save_submission_and_comment_data_to_db


# This section calls the other functions responsible for
# extracting the data from reddit


def extract_data_from_reddit(reddit, db_conn, sub_name, keyword):
    log("extracting data...", constants.msg_info)

    # check keyword across subreddit's submissions
    log(f"checking submission...", constants.msg_info)
    check_keyword_from_submissions(reddit, db_conn, sub_name, keyword)

    # check keyword across subreddit's comments
    log(f"checking comment...", constants.msg_info)
    check_keyword_from_comments(reddit, db_conn, sub_name, keyword)


# This section deals with reddit submissions from a particular subreddit
def check_keyword_from_submissions(reddit, db_conn, sub_name, keyword):
    categories = ['hot', 'top', 'new']
    for sub_category in categories:
        if sub_category == 'hot':
            log(f"[{constants.sub_hot}] submission", constants.msg_info)
            submissions = reddit.subreddit(sub_name).hot()
        elif sub_category == 'top':
            log(f"[{constants.sub_top}] submission", constants.msg_info)
            submissions = reddit.subreddit(sub_name).top()
        elif sub_category == 'new':
            log(f"[{constants.sub_new}] submission", constants.msg_info)
            submissions = reddit.subreddit(sub_name).new()
        else:
            return

        for submission in submissions:
            # check if the keyword is present in submission
            if re.search(keyword, submission.title, re.IGNORECASE):
                # save the found submissions data in the db
                extracted_data = {
                    'record_id': submission.id,
                    'content': submission.title
                }
                save_submission_and_comment_data_to_db(db_conn, constants.submission_category, extracted_data)


# This section deals with reddit comments from a particular subreddit
def check_keyword_from_comments(reddit, db_conn, sub_name, keyword):
    for comment in reddit.subreddit(sub_name).comments(limit=1000):
        if re.search(keyword, comment.body, re.IGNORECASE):
            # save the found comment ids in the db
            extracted_data = {
                'record_id': comment.id,
                'content': comment.body
            }
            save_submission_and_comment_data_to_db(db_conn, constants.comment_category, extracted_data)
