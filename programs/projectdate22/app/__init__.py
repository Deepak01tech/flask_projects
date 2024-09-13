from flask import Flask
from .auth import auth as auth_blueprint
from .main import main as main_blueprint
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy




def create_app():
    app = Flask(__name__,template_folder="../templates")

    app.config["SECRET_KEY"] = 'secret-key'
    app.config["SQLALCHEMY_DATABASE_URL"] = 'sqlite:///db.sqlite'

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)