#!/usr/bin/python3
'''
final project api
'''
from flask import Flask, render_template, abort, make_response, jsonify
from flask_cors import CORS
from api.v1.views import app_views

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    apiHost = "0.0.0.0"
    apiPort = 5000
    app.run(host=apiHost, port=int(apiPort), threaded=True)
