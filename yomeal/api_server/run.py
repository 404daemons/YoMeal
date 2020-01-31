import os
from flask import Flask
import argparse
from config_sample import APP_CONFIG_MAPPER


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(APP_CONFIG_MAPPER[config_name])
    print('*** Running config {}...'.format(config_name.upper()))

    # Import modules.
    from modules.basic.routes import mod as webapp
    from modules.nutrition.routes import mod as nutrition
    from modules.parser.routes import mod as parser
    from modules.sms_handle.routes import mod as sms

    # Register modules via blue prints.
    app.register_blueprint(webapp)
    app.register_blueprint(nutrition)
    app.register_blueprint(parser)
    app.register_blueprint(sms)

    return app


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--instance_mode', metavar='instance_mode',
                        dest='instance_mode', default="local",
                        help="Server Instance Mode.")
    parser.add_argument('-p', '--port', metavar='port', dest='port',
                        help="Server port", default="3300")

    args = parser.parse_args()

    app = create_app(args.instance_mode)
    app.run(port=int(args.port))
