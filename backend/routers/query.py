from fastapi import APIRouter, Depends, HTTPException, Form, UploadFile, File
from sqlalchemy.orm import Session
from .. import models, schemas, database
from ..services import vector_db, gemini, weather
from ..auth_utils import verify_password # Placeholder if we need auth util access
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from ..auth_utils import SECRET_KEY, ALGORITHM

router = APIRouter(
    prefix="/api/v1/query",
    tags=["Query"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        phone_number: str = payload.get("sub")
        if phone_number is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db.query(models.User).filter(models.User.phone_number == phone_number).first()
    if user is None:
        raise credentials_exception
    return user

@router.post("/submit", response_model=schemas.QueryResponse)
async def submit_query(
    input_type: str = Form(...),
    original_input: str = Form(...),
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    # Mock User for Debugging
    # current_user = models.User(id=1, location="Kerala", crops_grown="Coconut")
    try:
        # 1. Retrieve Context
        print(f"DEBUG: Searching Vector DB for: {original_input}")
        context = vector_db.search_knowledge_base(original_input)
        print(f"DEBUG: Context Retrieved (Length: {len(context) if context else 0})")
        
        # 2. Update Context with User Profile + Weather Mock
        # 2. Update Context with User Profile + Real Weather
        weather_info = await weather.get_current_weather(current_user.location)
        print(f"DEBUG: Weather Info: {weather_info}")
        
        full_context = f"User Profile: Location={current_user.location}, Crops={current_user.crops_grown}.\n{weather_info}\n\nKnowledge Base:\n{context}"
        
        # 3. Generate Answer
        print("DEBUG: Calling Gemini API...")
        answer = gemini.generate_rag_response(original_input, full_context)
        print("DEBUG: Gemini Response Received")
        
        # 4. Save to DB
        new_query = models.Query(
            user_id=current_user.id,
            input_type=input_type,
            original_input=original_input,
            enriched_prompt=full_context,
            ai_response_text=answer,
            status=models.QueryStatus.SOLVED,
            confidence_score=0.9 # Mock score for now
        )
        db.add(new_query)
        db.commit()
        db.refresh(new_query)
        
        return new_query
    except Exception as e:
        print(f"CRITICAL ERROR in submit_query: {str(e)}")
        import traceback
        with open("backend/crash.log", "w") as f:
            f.write(f"Error: {str(e)}\n")
            f.write(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
