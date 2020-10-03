from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
from flask_uploads import UploadSet,configure_uploads,IMAGES

#from config import config_options


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
photos = UploadSet('photos',IMAGES)
simple = SimpleMDE()


app = Flask(__name__, instance_relative_config=True)


# Setting up configuration
app.config.from_object(DevConfig)

# Initializing flask extensions
bootstrap.init_app(app)
db.init_app(app)
login_manager.init_app(app)
mail.init_app(app)
simple.init_app(app)


# Registering the blueprint
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

from app import views


if __name__ == '__main__':
    app.run()


