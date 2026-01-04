from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth, query

# Create Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="iFarmAssist API",
    description="Backend API for iFarmAssist - AI Powered Farm Assistant",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Exception Handler Middleware
from fastapi import Request
from fastapi.responses import JSONResponse
import traceback

@app.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        error_msg = f"GLOBAL CRASH: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        with open("backend/global_crash.log", "w") as f:
            f.write(error_msg)
        return JSONResponse(status_code=500, content={"detail": f"Internal Server Error: {str(e)}"})

# Include Routers
app.include_router(auth.router)
app.include_router(query.router)

@app.get("/", tags=["General"])
async def root():
    return {
        "message": "Welcome to iFarmAssist API",
        "status": "active",
        "version": "1.0.0"
    }

@app.get("/health", tags=["General"])
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    # Print Registered Routes for Debugging
    print("Registered Routes:")
    for route in app.routes:
        print(f" - {route.path} [{route.name}]")

    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
