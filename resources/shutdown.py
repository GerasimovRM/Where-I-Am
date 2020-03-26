from flask import request, current_app, Blueprint, jsonify
from flask_restful import Resource


class Shutdown(Resource):
    @staticmethod
    def __shutdown_server():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()

    def get(self):
        Shutdown.__shutdown_server()
        return jsonify(answer='Server shutting down...')
