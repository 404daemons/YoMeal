from flask import request, Blueprint

mod = Blueprint('WebApp', __name__, url_prefix="/")


@mod.route('/', methods=['GET'])
def web_samepl():
    return "Hello World! from Web-App."