from flask import Flask, Response
from flask_cors import CORS
from message_announcer import MessageAnnouncer
import logging

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)
announcer = MessageAnnouncer()

def format_sse(data: str, event=None) -> str:
    msg = f'data: {data}\n\n'
    if event is not None:
        msg = f'event: {event}\n{msg}'
    return msg

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-transform"
    return r

@app.route('/listen', methods=['GET'])
def listen():
    LOGGER.info('New client listening')
    def stream():
        messages = announcer.listen()  # returns a queue.Queue
        while True:
            msg = messages.get()  # blocks until a new message arrives
            LOGGER.info(f"Got msg: {msg}")
            yield msg

    return Response(stream(), mimetype='text/event-stream')

@app.route('/ping')
def ping():
    msg = format_sse(data='pong')
    announcer.announce(msg=msg)
    return {}, 200