from flask import jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity, create_access_token

from sqlalchemy.exc import SQLAlchemyError

from models import db_session
from models.user import User


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        """
        Refresh jwt-token
        """
        
        user_id = get_jwt_identity()
        access_token = create_access_token(identity=user_id)
        return jsonify(access_token=access_token)