import datetime
import json
import logging
import os

from db_models import Activity
from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
from mongoengine.queryset.visitor import Q as MongoQuery

DATE_FMT = '%Y-%m-%d %H:%M:%S'

log = logging.getLogger()
app_dir = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=os.path.join(app_dir, 'mongo.app.log'),
                    filemode='a',
                    format='%(asctime)s, %(levelname)s %(message)s',
                    datefmt='%H:%M:%S', level=logging.DEBUG)


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(status=200, message='MongoDB app!', data=[])


@app.route('/activity', methods=['POST'])
def add_activity():
    data_dict = request.get_json(force=True)
    if not isinstance(data_dict, dict):
        return jsonify(status=400, message="Invalid payload data. Data "
                                           "should be single JSON", data=[])
    _items = list()
    for item in data_dict['items']:
        _new_activity = Activity()
        _new_activity = _new_activity.from_json(json.dumps(item))
        try:
            _new_activity.validate()
        except Exception as e:
            log.error(e.to_dict())
            return jsonify(status=400, message=e.to_dict(), data=[])
        _items.append(_new_activity)
    Activity.objects.insert(_items)
    msg = "Total {} activities added successfully.".format(len(_items))
    log.info(msg)
    return jsonify(status=200, message=msg, data=[])


@app.route('/activity/<int:ph_no>', methods=['POST'])
def get_activity(ph_no):
    data_dict = request.get_json(force=True)
    filters = MongoQuery(phone_no=ph_no)
    if 'start_date' in data_dict:
        _start_date = None
        try:
            _start_date = datetime.strptime(data_dict['start_date'], DATE_FMT)
        except ValueError:
            try:
                _start_date = datetime.strptime(data_dict['start_date'] +
                                                " 00:00:00", DATE_FMT)
            except:
                pass
        finally:
            if _start_date:
                filters = filters & MongoQuery(recorded_at__gt=_start_date)

    if 'end_date' in data_dict:
        _end_date = None
        try:
            _end_date = datetime.strptime(data_dict['end_date'], DATE_FMT)
        except ValueError:
            try:
                _end_date = datetime.strptime(data_dict['end_date'] +
                                              " 23:59:59", DATE_FMT)
            except:
                pass
        finally:
            if _end_date:
                filters = filters & MongoQuery(recorded_at__lt=_end_date)
    log.debug(filters)
    _activities = Activity.objects(filters)
    msg = 'User#{} fetched {} activities.'.format(ph_no, len(_activities))
    log.info(msg)
    return jsonify(status=200, message=msg, data=_activities.to_json())


@app.route('/activity/<int:ph_no>/<value>', methods=['GET'])
def get_summary_activity(ph_no, value):
    data_dict = request.get_json()
    rtn_dict = dict()
    filters = MongoQuery(phone_no=ph_no)
    if 'start_date' in data_dict:
        _start_date = None
        try:
            _start_date = datetime.strptime(data_dict['start_date'], DATE_FMT)
        except ValueError:
            try:
                _start_date = datetime.strptime(data_dict['start_date'] +
                                                " 00:00:00", DATE_FMT)
            except:
                pass
        finally:
            if _start_date:
                rtn_dict['start_date'] = _start_date
                filters = filters & MongoQuery(recorded_at__gt=_start_date)

    if 'end_date' in data_dict:
        _end_date = None
        try:
            _end_date = datetime.strptime(data_dict['end_date'], DATE_FMT)
        except ValueError:
            try:
                _end_date = datetime.strptime(data_dict['end_date'] +
                                              " 23:59:59", DATE_FMT)
            except:
                pass
        finally:
            if _end_date:
                rtn_dict['end_date'] = _end_date
                filters = filters & MongoQuery(recorded_at__lt=_end_date)

    log.debug(filters)
    _activities = Activity.objects(filters).sum(value)
    rtn_dict['phone_no'] = ph_no
    rtn_dict[value] = _activities
    log.info(rtn_dict)
    return jsonify(status=200, message="Success", data=rtn_dict)


if __name__ == "__main__":
    # Added as default config for now. Will change it in future.
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 5000)
    app.config['MONGODB_SETTINGS'] = {
        "db": "myapp",
    }
    db = MongoEngine(app)
    app.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
