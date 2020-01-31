from flask import request, Blueprint
from modules.nutrition import libs

mod = Blueprint('nutrition_app', __name__, url_prefix="/nutrition")


@mod.route('/')
@mod.route('/hello', methods=['GET'], strict_slashes=False)
def process_customer_config():
    return libs.get_welcome_message()