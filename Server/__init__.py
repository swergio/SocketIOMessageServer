"""
The flask application package.
"""

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)


#Server logging is set to ERROR only.

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


socketio = SocketIO(app)

import Server.views