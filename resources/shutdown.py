from flask import request, current_app, Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from models import db_session
from models.admin import Admin
from models.super_admin import SuperAdmin


class Shutdown(Resource):
    @staticmethod
    def __shutdown_server():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()

    @jwt_required
    def get(self):
        """
        Only for SuperAdmin: Shutdown server
        """
        current_user_id = get_jwt_identity()
        session = db_session.create_session()
        admin = session.query(Admin).filter(Admin.user_id==current_user_id).scalar()
        if session.query(SuperAdmin).filter(SuperAdmin.admin_id==admin.id).scalar():
            Shutdown.__shutdown_server()
            return jsonify(answer='Server shutting down...')
        return jsonify(answer='You are not super admin!')
