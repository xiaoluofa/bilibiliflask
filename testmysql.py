import time
from mysqllink import db
from mysqllink import cursor
from itertools import chain


while True:
    try:
        sql = "SELECT room_id FROM bilibili_uid"
        cursor.execute(sql)
        result = cursor.fetchall()
        room_id_new = list(chain.from_iterable(result))
        print(room_id_new)
    except Exception as e:
        db.rollback()
        print(e)
    time.sleep(1)