from flask import Flask
from .models import initialize_db
from flask_bcrypt import Bcrypt  # Correct import

def create_app():
    app = Flask(__name__, template_folder='../templates')

    # Secret key for session management, should be stored in environment variables for production
    app.secret_key = 'this_is_my_app'

    # Initialize the database
    initialize_db(app)

    # Initialize bcrypt for password hashing
    bcrypt = Bcrypt(app)  # Create an instance of Bcrypt with your app

    # Import and register blueprints
    from .routes import main
    from .auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix='/auth')

    return app
