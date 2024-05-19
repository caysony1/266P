from flask import Flask
from database.schema import create_db
from api.user_routes import user
from api.account_routes import account

flask = Flask(__name__)
    
if __name__ == '__main__':
    create_db()

    # register the flask endpoints
    flask.register_blueprint(user)
    flask.register_blueprint(account)
    flask.run()
