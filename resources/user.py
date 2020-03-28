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
        For auth users
        Access:
        1) Admins can see all
        2) Users can see user_id only if he in back_friends
        """
        current_user_id = get_jwt_identity()
        session = db_session.create_session()
        admin = session.query(Admin).filter(Admin.user_id==current_user_id).first()
        if admin:
            user = session.query(User).get(user_id)
            if not user:
                return make_response(jsonify({"error": "User not found"}), 404)
            return jsonify(code=501)
            return jsonify(user.to_dict())

        """
        current_user = session.query(User).get(current_user_id)
        back_friends = list(map(lambda u: u.id, current_user.back_friends))
        if user_id in back_friends:
            return jsonify(session.query(User).get(user_id).to_dict())
        return make_response(jsonify(error='Access denied!'), 401)
        """

    '''
    @jwt_required
    def post(self, user_id):
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
            return make_response(jsonify({"error": ex.args[0]}), 400)
    '''

