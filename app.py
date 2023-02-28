from flask import Flask
from blueprints.index import indexbp
from blueprints.channel import channelbp
from flask_cors import *
import config

import pymysql


app = Flask(__name__)
app.config.from_object(config)
CORS(app, supports_credentials=True)
# db.init_app(app)
#蓝图注册
app.register_blueprint(indexbp,url_prefix="/index")
# 相关配置
app.register_blueprint(channelbp,url_prefix="/channel")


# 创建组件对象
@app.route("/")
def indexc():

    dict = {
        "stattus": 200,
        "data": 123,
        "msg": "获取全部的book成功"
    }
    return dict


if __name__ == '__main__':
    app.run(DEBUG=True,use_reloader=False)


