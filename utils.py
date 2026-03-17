```python
# Import necessary libraries
import jwt
from flask import current_app

# Define utility functions
def generate_token(user_id):
    """Generate JWT token"""
    payload = {'user_id': user_id}
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

def verify_token(token):
    """Verify JWT token"""
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
```

###