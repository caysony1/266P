from flask import Blueprint, abort, request, jsonify
from flask_login import login_required

from services.account_service import AccountService

account = Blueprint('account', __name__)

@account.route('/account/view_balance', methods=['GET'])
@login_required
def view_balance():
    try:
        account_service = AccountService()
        balance = account_service.view_balance()
        return jsonify({ 'balance': balance }), 200
    except Exception as e:
        return abort(500, description='There is an issue fetching the balance: {}'.format(str(e)))
    
@account.route('/account/deposit', methods=['POST'])
@login_required
def deposit():
    try:
        request_data = request.get_json()
        account_service = AccountService()
        account_service.deposit(request_data.get('amount'))
        return jsonify({ 'message': 'withdraw success!' }), 200
    except Exception as e:
        return abort(500, description='There is an issue depositing money: {}'.format(str(e)))
    
@account.route('/account/withdraw', methods=['POST'])
@login_required
def withdraw():
    try:
        request_data = request.get_json()
        account_service = AccountService()
        account_service.withdraw(request_data.get('amount'))
        return jsonify({ 'message': 'withdraw success!' }), 200
    except Exception as e:
        return abort(500, description='There is an issue withdrawing money: {}'.format(str(e)))
