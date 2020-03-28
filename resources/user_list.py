from flask import jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db_session
from models.user import User
from models.admin import Admin

from sqlalchemy.exc import SQLAlchemyError

from .virtual import VirtualUser


class UserListResource(VirtualUser, Resource):
    @jwt_required
    def get(self):
        """
        Only for admins: Show all users
        """
        current_user_id = get_jwt_identity()
        session = db_session.create_session()
        admin = session.query(Admin).filter(Admin.user_id==current_user_id).first()
        if not admin:
            return make_response(jsonify(error='Access denied: You are not admin'), 401)
        answer = []
        for user in session.query(User).all():
            friends = list(map(lambda u: u.id, user.friends))
            back_friends = list(map(lambda u: u.id, user.back_friends))
            answer.append(user.to_dict(only=['id', 'nickname', 'last_name', 'first_name', 'middle_name']))
            answer[-1]['friends'] = friends
            answer[-1]['back_friends'] = back_friends
        return jsonify(users=answer)

    @jwt_required
    def post(self):
        """
        Only for admins: Add user
        """

        current_user_id = get_jwt_identity()
        session = db_session.create_session()
        admin = session.query(Admin).filter(Admin.user_id == current_user_id).first()
        if not admin:
            return make_response(jsonify(error='Access denied: You are not admin'), 401)
        args = self.parser.parse_args()
        try:
            user = User(**args)
            session.add(user)
            session.commit()
            return jsonify({'success': 'OK'})
        except SQLAlchemyError as ex:
            session.rollback()
            return make_response(jsonify({"error": ex.args}), 400)
