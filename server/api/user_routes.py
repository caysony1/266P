from flask import Blueprint, abort, request, jsonify
from services.auth_service import AuthService

user = Blueprint('user', __name__)

@user.route('/login', methods=['POST'])
def login():
    try:
        request_data = request.get_json()
        
        auth_service = AuthService()

        auth_service.login(
            request_data.get('username'),
            request_data.get('password'),
        )

        return jsonify({ 'message': 'Login success!' }), 200
    except:
        return jsonify({ 'message': 'Login failed!' }), 200

@user.route('/register', methods=['POST'])
def register():
    try:
        request_data = request.get_json()
        
        auth_service = AuthService()

        auth_service.register(
            request_data.get('username'),
            request_data.get('password'),
            request_data.get('firstname'),
            request_data.get('lastname'),
            request_data.get('balance')
        )

        return jsonify({ 'message': 'Account registration - Success!' }), 200
    except:
        return abort(400, description = 'Account registration - Failed!')