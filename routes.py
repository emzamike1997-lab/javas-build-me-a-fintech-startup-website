```python
# Import necessary libraries
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import User, Account, Transaction
from .schemas import UserResponse, AccountResponse, TransactionResponse, ErrorResponse
from .utils import generate_token, verify_token
from . import db

# Define API routes
api = Blueprint('api', __name__)

# User registration
@api.route('/register', methods=['POST'])
def register():
    """Register user"""
    data = request.get_json()
    user = UserCreate(**data)
    existing_user = User.query.filter_by(username=user.username).first()
    if existing_user:
        return jsonify(ErrorResponse(error='username_taken', message='Username is already taken').dict()), 400
    new_user = User(username=user.username, email=user.email, password=user.password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(UserResponse(id=new_user.id, username=new_user.username, email=new_user.email).dict()), 201

# User login
@api.route('/login', methods=['POST'])
def login():
    """Login user"""
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or user.password != data['password']:
        return jsonify(ErrorResponse(error='invalid_credentials', message='Invalid username or password').dict()), 401
    token = generate_token(user.id)
    return jsonify({'token': token}), 200

# Account creation
@api.route('/accounts', methods=['POST'])
@jwt_required
def create_account():
    """Create account"""
    user_id = get_jwt_identity()
    data = request.get_json()
    account = AccountCreate(**data)
    existing_account = Account.query.filter_by(account_number=account.account_number).first()
    if existing_account:
        return jsonify(ErrorResponse(error='account_number_taken', message='Account number is already taken').dict()), 400
    new_account = Account(user_id=user_id, account_number=account.account_number, balance=0.0)
    db.session.add(new_account)
    db.session.commit()
    return jsonify(AccountResponse(id=new_account.id, user_id=new_account.user_id, account_number=new_account.account_number, balance=new_account.balance).dict()), 201

# Transaction creation
@api.route('/transactions', methods=['POST'])
@jwt_required
def create_transaction():
    """Create transaction"""
    user_id = get_jwt_identity()
    data = request.get_json()
    transaction = TransactionCreate(**data)
    account = Account.query.filter_by(user_id=user_id, account_number=data['account_number']).first()
    if not account:
        return jsonify(ErrorResponse(error='account_not_found', message='Account not found').dict()), 404
    new_transaction = Transaction(account_id=account.id, transaction_type=transaction.transaction_type, amount=transaction.amount)
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify(TransactionResponse(id=new_transaction.id, account_id=new_transaction.account_id, transaction_type=new_transaction.transaction_type, amount=new_transaction.amount, timestamp=str(new_transaction.timestamp)).dict()), 201

# Balance inquiry
@api.route('/balance', methods=['GET'])
@jwt_required
def get_balance():
    """Get balance"""
    user_id = get_jwt_identity()
    account = Account.query.filter_by(user_id=user_id).first()
    if not account:
        return jsonify(ErrorResponse(error='account_not_found', message='Account not found').dict()), 404
    return jsonify({'balance': account.balance}), 200
```

###