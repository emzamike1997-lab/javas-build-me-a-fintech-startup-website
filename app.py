```python
# Import necessary libraries
from flask import Flask
from flask_jwt_extended import JWTManager
from . import db, api

# Create Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fintech.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'secret_key'

# Initialize SQLAlchemy and JWTManager
db.init_app(app)
jwt = JWTManager(app)

# Register API routes
app.register_blueprint(api)

# Run app
if __name__ == '__main__':
    app.run(debug=True)
```

###