from flask import Flask, request
from sms_handler import handler
app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_handler_route():
    if request.method == 'POST':
        return handler.read_sms(request.form)
    else:
        return "Wrong method"


@app.route('/')
def hello():
    return "Begining of YoMeal!"


if __name__ == '__main__':
    app.run(debug=True)
