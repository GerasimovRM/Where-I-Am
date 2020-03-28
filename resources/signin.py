from flask import jsonify, make_response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token

import datetime

from models import db_session
from models.user import User

from .virtual import VirtualUser


class SigninResource(Resource):
    def post(self):
        """
        For all: Login
        """
        args = request.get_json()
        session = db_session.create_session()

        user = session.query(User).filter(User.nickname==args['nickname']).first()
        if not user:
            return make_response(jsonify(error='Invalid nickname'), 401)

        auth = user.check_password(args['unhashed_password'])
        if not auth:
            return make_response(jsonify(error='Invalid password'), 401)


        exp_access = datetime.timedelta(days=1)
        exp_refresh = datetime.timedelta(hours=1)
        access_token = create_access_token(identity=str(user.id), expires_delta=exp_access)
        refresh_token = create_refresh_token(identity=str(user.id), expires_delta=exp_refresh)
        return jsonify(access_token=access_token, refresh_token=refresh_token)


