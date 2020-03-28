from flask import Blueprint
from flask_restful import Api

from resources import CurrentUserResource, UserListResource, Shutdown, SignupResource, SigninResource
from resources import UserResource, AdminListResource

api_v1 = Blueprint('api_v1', __name__)

api = Api(api_v1)

api.add_resource(UserResource, '/user/<int:user_id>')
api.add_resource(CurrentUserResource, '/user')
api.add_resource(UserListResource, '/users')

api.add_resource(Shutdown, '/shutdown')
api.add_resource(SignupResource, '/signup')
api.add_resource(SigninResource, '/signin')

api.add_resource(AdminListResource, '/admins')

