from flask import jsonify
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from models import db_session
from models.user import User

from .virtual import VirtualUser


class FriendsListResource(Resource):
    @jwt_required
    def get(self):
        """
        For auth user: Get user back_friends
        """
        current_user_id = get_jwt_identity()
        session = db_session.create_session()
        friends = session.query(User).get(current_user_id).friends
        return jsonify(friends=[friend.to_dict() for friend in friends])
