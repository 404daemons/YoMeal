from flask import Flask, request
from sms_handler.handler import SMS
app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_handler_route():
    sms = SMS()
    if request.method == 'POST':
        return sms.readSMS(request.form)
    else:
        return "Wrong method"


@app.route('/')
def hello():
    return "Begining of YoMeal!"


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, threaded=True, host='0.0.0.0', port=5000)
