from flask import Flask, make_response, jsonify
from flask_jwt_extended import JWTManager


from models import db_session
from models.user import User


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    db_file = app.config['SQLALCHEMY_DATABASE_URI']
    db_session.global_init(db_file)

    jwt = JWTManager(app)

    from routes import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Request not found'}), 404)

    return app
