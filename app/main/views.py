from flask import jsonify

from . import main


@main.route("/")
def hello():
    response = dict()
    response['message'] = 'hello'
    return jsonify(response), 200
