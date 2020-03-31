from flask import jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from models import db_session
from models.admin import Admin


class AdminListResource(Resource):
    @jwt_required
    def get(self):
        """
        Only for Admins: Show admins
        """
        current_user_id = get_jwt_identity()
        session = db_session.create_session()
        admin = session.query(Admin).filter(Admin.user_id == current_user_id).first()
        if not admin:
            return make_response(jsonify(error='Access denied: You are not admin'), 401)

        admins = session.query(Admin).all()
        return jsonify(admins=[admin.user.to_dict() for admin in admins])

    def post(self):
        """
        Only for SuperAdmins: Add admin
        """
        # TODO
        pass