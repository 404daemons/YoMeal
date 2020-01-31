from flask import request, Blueprint

mod = Blueprint('ParserApp_', __name__, url_prefix="/parser")

@mod.route('/')
@mod.route('/hello', methods=['GET'], strict_slashes=False)
def message_sample():
    return "Hello World API from Parser App."