from flask import jsonify, make_response
from flask_restful import Resource

from sqlalchemy.exc import SQLAlchemyError

from models import db_session
from models.user import User

from .virtual import VirtualUser


class SignupResource(VirtualUser, Resource):
    def post(self):
        """
        For all: Registration
        """

        args = self.parser.parse_args()
        session = db_session.create_session()
        try:
            new_user = User(**args)
            session.add(new_user)
            session.commit()
        except SQLAlchemyError as ex:
            session.rollback()
            return make_response(jsonify({"error": ex.args}), 400)
        return jsonify(id=new_user.id)
