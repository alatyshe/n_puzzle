from flask import Flask
from config import Config
import os


app = Flask(__name__)
app._static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
app.config.from_object(Config)

from app import views
