from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from .. import models, schemas, auth_utils, database

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)

@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    print(f"DEBUG: Registering user {user.phone_number}")
    db_user = db.query(models.User).filter(models.User.phone_number == user.phone_number).first()
    if db_user:
        print("DEBUG: User already exists")
        raise HTTPException(status_code=400, detail="Phone number already registered")
    
    print("DEBUG: Hashing password...")
    hashed_password = auth_utils.get_password_hash(user.password)
    print("DEBUG: Password hashed. Creating DB object...")
    
    new_user = models.User(
        phone_number=user.phone_number,
        hashed_password=hashed_password,
        role=user.role,
        full_name=user.full_name,
        location=user.location,
        crops_grown=user.crops_grown
    )
    print("DEBUG: Adding to session...")
    db.add(new_user)
    print("DEBUG: Committing to DB...")
    db.commit()
    print("DEBUG: Refreshing...")
    db.refresh(new_user)
    print("DEBUG: Registration Complete")
    return new_user

@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    # OAuth2PasswordRequestForm expects 'username', we use 'phone_number' as username
    user = db.query(models.User).filter(models.User.phone_number == form_data.username).first()
    if not user or not auth_utils.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect phone number or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=auth_utils.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_utils.create_access_token(
        data={"sub": user.phone_number, "role": user.role.value}, # Store role in token
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
