import os
import mysql.connector as mysql
import constants

from dotenv import load_dotenv
from mysql.connector import errorcode
from logger import log

# load env variables
load_dotenv()

"""
Establish connection to the db
"""


def create_db_connection():
    host = os.environ.get('MYSQL_HOST')
    database = os.environ.get('MYSQL_DATABASE')
    user = os.environ.get('MYSQL_USER')
    password = os.environ.get('MYSQL_PASSWORD')
    try:
        connection = mysql.connect(
            host=host,
            database=database,
            user=user,
            password=password)

        log("connected successfully", constants.msg_info)
        return connection
    except mysql.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            log("Access denied:Please recheck your username/password", constants.msg_info)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            log("Database does not exist", constants.msg_info)
        else:
            log(err, constants.msg_info)