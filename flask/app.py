from flask import Flask
import requests
import os, sys
import logging

application = app = Flask(__name__)

# tying the logger with gunicorn logging
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
logging.getLogger().setLevel(logging.INFO)

@app.route('/')
def default():
    path = sys.path
    return "[Flask] healthcheck:: PATH:: " + str(path)


# test http instrumentation
@app.route('/outgoing-http-call')
def callHTTP():
    app.logger.info("Hello from outgoing-http-call")
    requests.get("https://aws.amazon.com")
    return "Ok! tracing outgoing http call"


if __name__ == "__main__":
    address = os.environ.get('LISTEN_ADDRESS')

    if address is None:
        host = '127.0.0.1'
        port = '5000'
    else:
        host, port = address.split(":")
    app.run(host=host, port=int(port), debug=False)