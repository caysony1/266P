from flask import Blueprint, abort, request, jsonify
from flask_login import login_required, current_user

from services.auth_service import AuthService
from services.account_service import AccountService

account = Blueprint('account', __name__)

@account.route('/account/view_balance', methods=['GET'])
@login_required
def view_balance():
    try:
        account_service = AccountService(current_user.get_id())
        balance = account_service.view_balance()
        return jsonify({ 'balance': balance }), 200
    except Exception as e:
        return abort(500, description='There is an issue fetching the balance: {}'.format(str(e)))
    
@account.route('/account/deposit', methods=['POST'])
@login_required
def deposit():
    try:
        account_service = AccountService(current_user.get_id())
        request_data = request.get_json()
        amount = request_data.get('amount')

        account_service.deposit(amount)

        return jsonify({ 
            'message': 'deposit success!'
        }), 200
    except Exception as e:
        return abort(500, description='There is an issue depositing money: {}'.format(str(e)))
    
@account.route('/account/withdraw', methods=['POST'])
@login_required
def withdraw():
    try:
        account_service = AccountService(current_user.get_id())
        request_data = request.get_json()
        amount = request_data.get('amount')
        
        account_service.withdraw(amount)

        return jsonify({ 
            'message': 'withdraw success!'
        }), 200
    except Exception as e:
        return abort(500, description='There is an issue withdrawing money: {}'.format(str(e)))
    
@account.route('/account/view_email', methods=['GET'])
@login_required
def view_email():
    try:
        auth_service = AuthService()
        user = auth_service.get_user(current_user.get_id())
        email_address = user.get('email')
        return jsonify({ 'email': email_address }), 200
    except Exception as e:
        return abort(500, description='There is an issue fetching email info: {}'.format(str(e)))
