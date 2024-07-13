#!/usr/bin/python3
"""
Web Server
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return make_response(jsonify({"error": "Not found"}), 404)


@app_views.route('/status', strict_slashes=False)  # Define the status route within the blueprint
def status():
    """
    Return the status of the API
    """
    return jsonify({"status": "OK"})


if __name__ == "__main__":
    # python -m api.v1.app 
    app.run(host="0.0.0.0", port=5000)
