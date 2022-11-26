import praw
import os
from dotenv import load_dotenv

# load env variables
# load_dotenv('/home/jkmdroid/python-bots/reddit/luxury/.env')
load_dotenv()

# initialize necessary variables
app_id = os.environ.get('APP_ID')
app_secret = os.environ.get('APP_SECRET')
password = os.environ.get('REDDIT_PASSWORD')
username = "jkm_droid_2496"
user_agent = "battles station by u/jkm_droid_2496"  # <platform>:<app ID>:<version string> (by u/<Reddit username>)


def create_reddit():
    # creat a reddit instance
    reddit = praw.Reddit(
        client_id=app_id,
        client_secret=app_secret,
        password=password,
        user_agent=user_agent,
        username=username
    )

    return reddit
