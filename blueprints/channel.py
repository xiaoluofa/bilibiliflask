import json
import sys
from datetime import datetime
import io
from flask import Blueprint
from sqlalchemy import text
import time
from mysqllink import db
from mysqllink import cursor
from itertools import chain

#
channelbp = Blueprint("channelbp",__name__)
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

@channelbp.route("/")
def channel():
    g_list= []
    try:
        sql = ("SELECT * FROM livestateinfo,(SELECT uid,name FROM (select * from userinfo as u inner join (\n"
               "select uid as uid2,max(time) as ctime  from userinfo group by uid) as uu\n"
               "on u.uid=uu.uid2\n"
               "and u.time=uu.ctime) as t) as g WHERE end_time = '2099-12-31 12:00:00' and livestateinfo.uid = g.uid")
        cursor.execute(sql)
        result = cursor.fetchall()
        # g = list(chain.from_iterable(result))
        print(result)
        print(type(result))
    except Exception as e:
        db.rollback()
        print(e)

    return result
# from exts import db
# from models import bilibili_uid, livestateinfo