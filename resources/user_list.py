from flask import jsonify, make_response, current_app
from flask_restful import reqparse, abort, Api, Resource
from sqlalchemy import exc

from models import db_session
from models.user import User

from sqlalchemy.exc import SQLAlchemyError


"""
TODO: NOT USE NOW!!
"""
class UserListResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nickname', required=True)
        self.parser.add_argument('first_name', required=True)
        self.parser.add_argument('middle_name')
        self.parser.add_argument('last_name', required=True)
        self.parser.add_argument('email', required=True)
        self.parser.add_argument('unhashed_password', required=True)
        self.parser.add_argument('registration_date')

    def get(self):
        session = db_session.create_session()
        answer = []
        for user in session.query(User).all():
            friends = list(map(lambda u: u.id, user.friends))
            back_friends = list(map(lambda u: u.id, user.back_friends))
            answer.append(user.to_dict(only=['id', 'nickname', 'last_name', 'first_name', 'middle_name']))
            answer[-1]['friends'] = friends
            answer[-1]['back_friends'] = back_friends
        return jsonify(users=answer)

    def post(self):
        session = db_session.create_session()
        args = self.parser.parse_args()
        try:
            user = User(**args)
            session.add(user)
            session.commit()
            return jsonify({'success': 'OK'})
        except SQLAlchemyError as ex:
            current_app.logger.error(ex)
            session.rollback()
            return make_response(jsonify({"error": ex.args[0]}), 400)

