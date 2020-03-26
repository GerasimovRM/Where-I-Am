from flask import Flask, make_response, jsonify

from .extensions import login_manager

from models import db_session
from models.user import User


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    db_file = app.config['SQLALCHEMY_DATABASE_URI']
    db_session.global_init(db_file)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    from routes import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    return app
