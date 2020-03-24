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


    def post(self):
        session = db_session.create_session()
        args = self.parser.parse_args()
        try:
            user = User(nickname=args['nickname'],
                        first_name=args['first_name'],
                        last_name=args['last_name'],
                        email=args['email'],
                        unhashed_password=args['unhashed_password'])
            if 'middle_name' in args:
                user.middle_name = args['middle_name']
            if 'registration_date' in args:
                user.registration_date = args['registration_date']
            session.add(user)
            session.commit()
            return jsonify({'success': 'OK'})
        except SQLAlchemyError as ex:
            current_app.logger.error(ex)
            session.rollback()
            return make_response(jsonify({"error": ex.args}), 400)

