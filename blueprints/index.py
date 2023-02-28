from flask import Blueprint

#
indexbp = Blueprint("indexbp",__name__)


@indexbp.route("/index")
def index():
    return '牛顿'

@indexbp.route("/channel/<int:roomid>")
def channelUid(roomid):
    channel = {
        "stattus": 200,
        "data": 123,
        "msg": roomid
    }
    return channel