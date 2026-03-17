```python
# Import necessary libraries
import os

# Define configuration
class Config:
    """Config class"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
```

### Running the Application
To run the application, navigate to the project directory and execute the following commands:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
The application will start on `http://localhost:5000`. You can use a tool like `curl` or a REST client to test the API endpoints.

### API Endpoints
The following API endpoints are available:
- `POST /register`: Register a new user
- `POST /login`: Login an existing user
- `POST /accounts`: Create a new account
- `POST /transactions`: Create a new transaction
- `GET /balance`: Get the balance of the current user's account

### Example Use Cases
- Register a new user: `curl -X POST -H "Content-Type: application/json" -d '{"username": "john", "email": "john@example.com", "password": "password"}' http://localhost:5000/register`
- Login an existing user: `curl -X POST -H "Content-Type: application/json" -d '{"username": "john", "password": "password"}' http://localhost:5000/login`
- Create a new account: `curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -d '{"account_number": "1234567890"}' http://localhost:5000/accounts`
- Create a new transaction: `curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -d '{"transaction_type": "deposit", "amount": 100.0, "account_number": "1234567890"}' http://localhost:5000/transactions`
- Get the balance of the current user's account: `curl -X GET -H "Authorization: Bearer <token>" http://localhost:5000/balance`