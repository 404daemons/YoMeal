from flask import request, Blueprint

mod = Blueprint('SMSApp', __name__, url_prefix="/sms/")

@mod.route('/')
@mod.route('/hello', methods=['GET'], strict_slashes=False)
def parser_sample():
    return "Hello World API from SMS App."