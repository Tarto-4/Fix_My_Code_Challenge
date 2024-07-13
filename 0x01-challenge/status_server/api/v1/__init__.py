from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')  # Use '/api/v1' prefix

from .views.index import *  # Import the status route from index.py
