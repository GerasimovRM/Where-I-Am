from flask import jsonify, make_response, current_app
from flask_restful import reqparse, abort, Api, Resource
from sqlalchemy import exc

from models import db_session
from models.user import User

from sqlalchemy.exc import SQLAlchemyError


"""
TODO: NOT USE NOW!!
"""
class UserResource(Resource):
    """
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nickname', required=True)
        self.parser.add_argument('first_name', required=True)
        self.parser.add_argument('middle_name')
        self.parser.add_argument('last_name', required=True)
        self.parser.add_argument('email', required=True)
        self.parser.add_argument('unhashed_password', required=True)
        self.parser.add_argument('registration_date')
    """


    def get(self, user_id):
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        friends = list(map(lambda u: u.id, user.friends))
        back_friends = list(map(lambda u: u.id, user.back_friends))
        answer = user.to_dict(only=['id', 'nickname', 'last_name', 'first_name', 'middle_name'])
        return jsonify(**answer, friends=friends, back_friends=back_friends)
