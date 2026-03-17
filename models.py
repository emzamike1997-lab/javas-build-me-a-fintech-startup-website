```python
# Import necessary libraries
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel
from datetime import datetime

# Initialize SQLAlchemy
db = SQLAlchemy()

# Define User model
class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    accounts = db.relationship('Account', backref='user', lazy=True)

# Define Account model
class Account(db.Model):
    """Account model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    account_number = db.Column(db.String(100), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0, nullable=False)
    transactions = db.relationship('Transaction', backref='account', lazy=True)

# Define Transaction model
class Transaction(db.Model):
    """Transaction model"""
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    transaction_type = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

# Define Pydantic models for validation
class UserCreate(BaseModel):
    """User create model"""
    username: str
    email: str
    password: str

class AccountCreate(BaseModel):
    """Account create model"""
    account_number: str

class TransactionCreate(BaseModel):
    """Transaction create model"""
    transaction_type: str
    amount: float
```

###