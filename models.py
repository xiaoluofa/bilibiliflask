# import datetime
# from exts import db
# import time
#
# class bilibili_uid(db.Model):
#     __tablename__ = "bilibili_uid"
#     uid = db.Column(db.String(255),primary_key=True)
#     room_id = db.Column(db.String(255),primary_key=True)
#
#     def __repr__(self) -> str:
#         return f'<bilibili_uid(uid:{self.uid} room_id:{self.room_id})>'
#
# class livechat(db.Model):
#     __tablename__ = "livechat"
#     senduid = db.Column(db.String(255),primary_key=True)
#     sendname = db.Column(db.String(255))
#     sendcontent = db.Column(db.String(255))
#     sendurl = db.Column(db.String(255))
#     room_id = db.Column(db.String(255))
#     time = db.Column(db.Date)
#     def __repr__(self):
#         return f'<livechat(senduid:{self.senduid} sendname:{self.sendname}sendcontent:{self.sendcontent}sendname:{self.sendurl}room_id:{self.room_id} time:{self.time})>'
#
# class livestateinfo(db.Model):
#     __tablename__ = "livestateinfo"
#     room_id = db.Column(db.String(255))
#     livetitle = db.Column(db.String(255))
#     liveface = db.Column(db.String(255))
#     livebackground = db.Column(db.String(255))
#     start_time = db.Column(db.Date)
#     end_time = db.Column(db.Date)
#     watch_show = db.Column(db.String(255))
#     uid = db.Column(db.String(255))
#     area_name = db.Column(db.String(255))
#     id = db.Column(db.Integer(),primary_key=True)
#     def __repr__(self):
#         return f'<livestateinfo(room_id:{self.room_id} livetitle:{self.livetitle}liveface:{self.liveface}livebackground:{self.livebackground}start_time:{self.start_time} end_time:{self.end_time}' \
#                f'watch_show:{self.watch_show}uid:{self.uid}area_name:{self.area_name}id:{self.id})>'
#
# class userinfo(db.Model):
#     __tablename__ = "userinfo"
#     uid = db.Column(db.String(255))
#     sex = db.Column(db.String(255))
#     follower = db.Column(db.Integer())
#     face = db.Column(db.String(255))
#     sign = db.Column(db.String(255))
#     level = db.Column(db.String(255))
#     time = db.Column(db.Date)
#     id = db.Column(db.Integer(), primary_key=True)
#     top_photo = db.Column(db.String(255))
#     def __repr__(self):
#         return f'<userinfo(uid:{self.uid} sex:{self.sex}follower:{self.follower}face:{self.face}sign:{self.sign} level:{self.level}' \
#                f'time:{self.time}id:{self.id}top_photo:{self.top_photo})>'