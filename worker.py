import re
import os
from logger import log
import constants


def get_data_from_submissions(submission, keyword, count, sub):
    log(f"checking {sub} submission {count}", constants.msg_info)
    # check if the keyword is present in submission
    if re.search(keyword, submission.title, re.IGNORECASE):
        count += 1

        # save the found submissions ids in text file
        if not os.path.isfile("submissions.txt"):
            with open("submissions.txt", 'a') as submission_ids:
                print("inside file not")
                submission_ids.write(submission.id)
                submission_ids.write("\n")
        # else:
        submission_ids = open("submissions.txt", 'r', encoding='utf-8')
        ids = submission_ids.read()

        if re.search(submission.id, ids):
            print("submission already exists")
            submission_ids.close()
        else:
            with open("submissions.txt", "a") as file:
                print("inside file")
                file.write(submission.id)
                file.write("\n")

    return count


def get_keywords_from_reddit(reddit, sub_name, keyword):
    log("extracting data...please wait", constants.msg_info)

    c_count = top_count = hot_count = 0
    # #check keyword across subreddit's top submissions
    for submission in reddit.subreddit(sub_name).top():
        top_count = get_data_from_submissions(submission, keyword, top_count, sub="top")

    # check keyword across subreddit's hot submissions
    for submission in reddit.subreddit(sub_name).hot():
        hot_count = get_data_from_submissions(submission, keyword, hot_count, sub="hot")

    # check keyword across subreddit's comments
    for comment in reddit.subreddit(sub_name).comments(limit=1000):
        # c_counter += 1

        log(f"checking comment {c_count}", constants.msg_info)
        if re.search(keyword, comment.body, re.IGNORECASE):
            c_count += 1

            # save the found comment ids in text file
            if not os.path.isfile("comments.txt"):
                with open("comments.txt", 'a') as comment_file:
                    print("inside file not-co")
                    comment_file.write(comment.id)
                    comment_file.write("\n")
            # else:
            comment_file = open("comments.txt", 'r', encoding='utf-8')
            ids = comment_file.read()

            if re.search(comment.id, ids):
                print("already exists")
                comment_file.close()
            else:
                with open("comments.txt", "a") as file:
                    print("inside file-co")
                    file.write(comment.id)
                    file.write('\n')
