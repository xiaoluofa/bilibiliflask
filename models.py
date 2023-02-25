import datetime
from exts import db
import time

class bilibili_uid(db.Model):
    __tablename__ = "bilibili_uid"
    uid = db.Column(db.String(255),primary_key=True)
    room_id = db.Column(db.String(255),primary_key=True)

    def __repr__(self) -> str:
        return f'<bilibili_uid(uid:{self.uid} room_id:{self.room_id})>'

class livechat(db.Model):
    __tablename__ = "livechat"
    senduid = db.Column(db.String(255),primary_key=True)
    sendname = db.Column(db.String(255))
    sendcontent = db.Column(db.String(255))
    sendurl = db.Column(db.String(255))
    room_id = db.Column(db.String(255))
    time = db.Column(db.Date)
    def __repr__(self):
        return f'<bilibili_uid(senduid:{self.senduid} sendname:{self.sendname}sendcontent:{self.sendcontent}sendname:{self.sendurl}room_id:{self.room_id} time:{self.time})>'
