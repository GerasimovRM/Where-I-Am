from flask import jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from models import db_session
from models.user import User
from models.user import friends_relation


class AddFriendResource(Resource):
    @jwt_required
    def post(self, friend_id):
        """
        For auth User: Add friend
        """
        current_user_id = get_jwt_identity()
        session = db_session.create_session()

        user = session.query(User).get(friend_id)
        print(user)
        if not user:
            return make_response(jsonify(error="User not found"), 404)

        current_user = session.query(User).get(current_user_id)
        if user in current_user.friends:
            return make_response(jsonify(error='Bad request: уже дружите'), 403)

        current_user.friends.append(user)
        session.commit()
        return jsonify(success='OK')

