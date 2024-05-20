from flask import Flask
from database.schema import create_db
from api.user_routes import user
from api.account_routes import account
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

flask = Flask(__name__)
login_manager = LoginManager(flask)

if __name__ == '__main__':
    create_db()

    # register the flask endpoints
    flask.register_blueprint(user)
    flask.register_blueprint(account)
    flask.run()
