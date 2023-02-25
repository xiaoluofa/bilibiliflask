from flask import Flask
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from blueprints.index import indexbp
import config
from exts import db
from models import bilibili_uid, livechat
import pymysql

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
app.register_blueprint(indexbp,url_prefix="/index")
# 相关配置



# 创建组件对象
@app.route("/")
def indexc():

    # g = db.session.query(bilibili_uid.uid).filter(bilibili_uid.room_id == 26545331).all()
    # print(g)
    # livechatnum = db.session.query(livechat).count()
    # print(livechatnum)
    # livechattime = db.session.query(livechat).order_by(livechat.time.desc()).first()
    # print(livechattime)

    dict = {
        "stattus": 200,
        "data": 123,
        "msg": "获取全部的book成功"
    }
    return dict


if __name__ == '__main__':
    app.run(DEBUG=True,use_reloader=False)


