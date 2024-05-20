from flask import Blueprint, abort, request, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user
from models.login_user import LoginUser
from services.auth_service import AuthService

auth = Blueprint('auth', __name__)
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    auth_service = AuthService()
    user = auth_service.get_user(user_id)
    return user

@auth.route('/login', methods=['POST'])
def login():
    try:
        request_data = request.get_json()
        
        new_session_user = LoginUser(
            request_data.get('username'),
            request_data.get('password'),
        )

        is_authenticated = login_user(new_session_user, False, None, False, False)

        if is_authenticated:
            return jsonify({ 'message': 'Login success!' }), 200
        else:
            return jsonify({ 'message': 'Login failed!' }), 200
    except:
        return abort(500, description = 'Login service issue!')

@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    try:
        is_logged_out = logout_user()

        if is_logged_out:
            return jsonify({ 'message': 'Logout success!' }), 200
        else:
            return jsonify({ 'message': 'Logout not successful!' }), 200   
    except:
        return abort(500, description = 'Log out service issue!')
    
@auth.route('/register', methods=['POST'])
def register():
    try:
        request_data = request.get_json()
        
        user_name = request_data.get('username')
        pass_word = request_data.get('password'),
        first_name = request_data.get('firstname'),
        last_name = request_data.get('lastname'),
        balance = request_data.get('balance')

        auth_service = AuthService()
        user_exists = auth_service.user_exists(user_name)

        if user_exists:
           return jsonify({ 'message': 'User already exists. Aborting.' }), 200

        auth_service.register(user_name, pass_word, first_name, last_name, balance)
        return jsonify({ 'message': 'Account registration - Success!' }), 200
    except:
        return abort(500, description = 'Account registration - Service issue!')