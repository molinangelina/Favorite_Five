#initializing anything we need/part of creation process
from flask import Flask
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

from . import routes