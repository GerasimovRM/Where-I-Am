from flask import jsonify, session
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from models import db_session
from models.user import User
from models.user import friends_relation


class FriendsRequestsResource(Resource):
    @jwt_required
    def get(self):
        """
        For auth User: Check friend requests
        """
        current_user_id = get_jwt_identity()
        session = db_session.create_session()

        user = session.query(User).get(current_user_id)
        back_friends = user.back_friends
        friends = user.friends
        request_friends = []
        for back_friend in back_friends:
            if back_friend not in friends:
                request_friends.append(back_friend)

        return jsonify(friends=[friend.to_dict() for friend in request_friends])
