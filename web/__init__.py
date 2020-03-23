from flask import Flask
# from flask_restful import res

from .extensions import login_manager

from .models import db_session
from .models.user import User

#from .routes import auth
#from .routes.main import main
from .routes.shutdown import shutdown




def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db_file = 'web/db/' + app.config['SQLALCHEMY_DATABASE_URI']
    db_session.global_init(db_file)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    app.register_blueprint(shutdown)
    # app.register_blueprint(main)
    # app.register_blueprint(auth)
    return app