from flask import jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db_session
from models.user import User
from models.admin import Admin

from sqlalchemy.exc import SQLAlchemyError

from .virtual import VirtualUser


class UserResource(VirtualUser, Resource):
    @jwt_required
    def get(self, user_id):
        """
        For auth users: Show user
        """
        current_user_id = get_jwt_identity()
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        if not user:
            return make_response(jsonify(error="User not found"), 404)
        return jsonify(user=user.to_dict())

