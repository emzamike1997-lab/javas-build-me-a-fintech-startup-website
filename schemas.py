```python
# Import necessary libraries
from pydantic import BaseModel
from typing import Optional

# Define schemas for API responses
class UserResponse(BaseModel):
    """User response model"""
    id: int
    username: str
    email: str

class AccountResponse(BaseModel):
    """Account response model"""
    id: int
    user_id: int
    account_number: str
    balance: float

class TransactionResponse(BaseModel):
    """Transaction response model"""
    id: int
    account_id: int
    transaction_type: str
    amount: float
    timestamp: str

class ErrorResponse(BaseModel):
    """Error response model"""
    error: str
    message: str
```

###