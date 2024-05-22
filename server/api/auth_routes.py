from flask import Blueprint, abort, jsonify, request, session
from flask_login import LoginManager, login_required, login_user, logout_user
from models.session_user import SessionUser
from services.auth_service import AuthService

auth = Blueprint('auth', __name__)
login_manager = LoginManager()

@login_manager.user_loader
def load_user(id: int):
    auth_service = AuthService()
    user = auth_service.get_user(id)

    if user is None:
        return None

    return SessionUser(
        user.get('id', 0),
        user.get('username', ''),
        user.get('first_name', ''),
        user.get('last_name', ''),
        user.get('email', '')
    )

@auth.route('/auth/login', methods=['POST'])
def login():
    try:
        request_data = request.get_json()
        user_name = request_data.get('username')
        password = request_data.get('password')

        auth_service = AuthService()
        is_valid = auth_service.is_valid_credentials(user_name, password)

        if is_valid == False:
            return jsonify({ 'message': 'Invalid username or password' }), 401

        user = auth_service.get_user_by_name(user_name)

        new_session_user = SessionUser(
            user.get('id', 0),
            user.get('username', ''),
            user.get('first_name', ''),
            user.get('last_name', ''),
            user.get('email', '')
        )

        login_user(new_session_user, False, None, False, True)
        return jsonify({ 'message': 'Log In - Success' }), 200
    except Exception as e:
        return abort(500, description='Log In - Failed: {}'.format(str(e)))

@auth.route('/auth/logout', methods=['GET'])
@login_required
def logout():
    try:
        session.clear()
        logout_user()
        return jsonify({ 'message': 'Logout success!' }), 200
    except Exception as e:
        return abort(500, description='Log In - Failed: {}'.format(str(e)))
    
@auth.route('/auth/register', methods=['POST'])
def register():
    try:
        request_data = request.get_json()
        
        user_name = request_data.get('username')
        pass_word = request_data.get('password')
        first_name = request_data.get('firstname')
        last_name = request_data.get('lastname')
        email = request_data.get('email')
        balance = request_data.get('balance')

        auth_service = AuthService()
        user_exists = auth_service.user_exists(user_name)

        if user_exists:
           return jsonify({ 'message': 'User already exists. Aborting.' }), 200

        auth_service.register(user_name, pass_word, first_name, last_name, email, balance)
        return jsonify({ 'message': 'Account registration - Success!' }), 200
    except Exception as e:
        return abort(500, description='There was an issue with registration: {}'.format(str(e)))