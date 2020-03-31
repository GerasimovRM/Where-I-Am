from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from models import db_session
from models.user import User


class CurrentUserResource(Resource):
    @jwt_required
    def get(self):
        """
        Get yourself data user
        """
        user_id = get_jwt_identity()
        session = db_session.create_session()
        return jsonify(current_user=session.query(User).get(user_id).to_dict())

    # TODO: put