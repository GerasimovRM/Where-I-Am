from flask import jsonify, session
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required

from models import db_session
from models.user import User

from .virtual import VirtualUser


class FriendsResource(VirtualUser, Resource):
    @jwt_required
    def get(self):
        """
        For auth user: Get friends
        """
        user_id = get_jwt_identity()
        db_context = db_session.create_session()
        user = db_context.query(User).get(user_id)
        friends = list(map(lambda u: u.id, user.friends))
        back_friends = list(map(lambda u: u.id, user.back_friends))
        answer = user.to_dict(only=['id', 'nickname', 'last_name', 'first_name', 'middle_name'])
        return jsonify(**answer, friends=friends, back_friends=back_friends)

    # TODO: delete

    # TODO: put