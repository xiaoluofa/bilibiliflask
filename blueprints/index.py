from flask import Blueprint




#
indexbp = Blueprint("indexbp",__name__)


@indexbp.route("/index")
def index():
    return '牛顿'