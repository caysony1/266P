from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from database.schema import create_db
from database.db_utils import add_default_accounts
from api.auth_routes import auth
from api.account_routes import account


flask = Flask(__name__)
flask.config['SECRET_KEY'] = 'lUBxSXchGZ'

# only allow the client side (localhost:3000) to access the server
# endpoints. does not matter the route within localhost:3000.
CORS(flask, resources={r'/*': {'origins': 'http://localhost:3000'}})

login_manager = LoginManager(flask)

# home page of the API server if one is interested
# to check if it is alive
@flask.route('/',)
def index():
    return 'Yes, it is me, the API server. I am alive and well.'

if __name__ == '__main__':
    create_db()
    add_default_accounts()

    # register the flask endpoints
    flask.register_blueprint(auth)
    flask.register_blueprint(account)
    login_manager.init_app(flask)
    flask.run()
