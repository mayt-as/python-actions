from flask import Flask
from flask import json
import logging
app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info('Main request successfull')  # log line
    return "Hello World!"


@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Status request successfull')  # log line
    return response


@app.route('/metrics')
def metrics():
    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {
                            "UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request successfull')  # log line
    return response


if __name__ == "__main__":
    # stream logs to app.log
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='127.0.0.1')
