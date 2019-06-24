import pymysql, json
from pymysql.cursors import DictCursor

with open("config.json") as f:
    CONFIG = json.load(f)["db_config"]


connection = pymysql.connect(
    host=CONFIG["host"],
    user=CONFIG["user"],
    password=CONFIG["password"],
    db=CONFIG["db"],
    charset=CONFIG["charset"],
    cursorclass=DictCursor
)