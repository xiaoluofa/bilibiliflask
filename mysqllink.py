import pymysql
from pymysql import cursors, converters
from pymysql.constants import FIELD_TYPE

conv = converters.conversions
conv[FIELD_TYPE.NEWDECIMAL] = float  # convert decimals to float
conv[FIELD_TYPE.DATE] = str  # convert dates to strings
conv[FIELD_TYPE.TIMESTAMP] = str  # convert dates to strings
conv[FIELD_TYPE.DATETIME] = str  # convert dates to strings


db = pymysql.connect(host='47.115.200.74', port=3306, user='root', passwd='112192', db='bilibili_data', charset='utf8',cursorclass=cursors.DictCursor)
cursor = db.cursor()

