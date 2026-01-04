from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from .models import UserRole, QueryStatus

# --- User Schemas ---
class UserBase(BaseModel):
    phone_number: str
    full_name: Optional[str] = None
    location: Optional[str] = None
    crops_grown: Optional[str] = None

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.FARMER

class UserLogin(BaseModel):
    phone_number: str
    password: str

class UserResponse(UserBase):
    id: int
    role: UserRole
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

# --- Token Schema ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    phone_number: Optional[str] = None

# --- Query Schemas ---
class QueryBase(BaseModel):
    input_type: str
    original_input: str
    heading: Optional[str] = None

class QueryCreate(QueryBase):
    pass

class QueryResponse(QueryBase):
    id: int
    user_id: int
    ai_response_text: Optional[str] = None
    confidence_score: float
    status: QueryStatus
    created_at: datetime
    media_url: Optional[str] = None

    class Config:
        from_attributes = True
