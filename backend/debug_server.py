from fastapi import FastAPI
import uvicorn
import sys

print("Initializing Debug App...")

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

if __name__ == "__main__":
    print("Starting Uvicorn...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
