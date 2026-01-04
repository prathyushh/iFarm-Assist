import requests
import time

BASE_URL = "http://127.0.0.1:8000"

def test_pipeline():
    # 1. Register
    print("1. Registering User...")
    user_data = {
        "phone_number": "9999999999",
        "password": "password123",
        "full_name": "Test Farmer",
        "role": "FARMER",
        "location": "Kerala",
        "crops_grown": "Coconut"
    }
    # Allow 400 if already exists
    try:
        res = requests.post(f"{BASE_URL}/api/v1/auth/register", json=user_data, timeout=10)
        print(f"Register Status: {res.status_code}")
    except requests.exceptions.Timeout:
        print("Register Timed Out!")
        return

    # 2. Login
    print("2. Logging In...")
    login_data = {
        "username": "9999999999",
        "password": "password123"
    }
    try:
        res = requests.post(f"{BASE_URL}/api/v1/auth/login", data=login_data, timeout=10)
        if res.status_code != 200:
            print(f"Login Failed: {res.text}")
            return
        
        token = res.json()["access_token"]
        print("Login Successful. Token received.")
    except requests.exceptions.Timeout:
        print("Login Timed Out!")
        return

    # 3. Submit Query
    print("3. Submitting RAG Query...")
    headers = {"Authorization": f"Bearer {token}"}
    query_data = {
        "input_type": "TEXT",
        "original_input": "What crops are suitable for Kerala climate?"
    }
    try:
        print("Note: First query may take up to 5 minutes (Model Download + API)...")
        print("Please be patient and do NOT close the window.")
        res = requests.post(f"{BASE_URL}/api/v1/query/submit", data=query_data, headers=headers, timeout=300) # 5 minute timeout
        
        if res.status_code == 200:
            print("Query Success!")
            print("Response:", res.json())
        else:
            print(f"Query Failed: {res.text}")
            with open("error_log.txt", "w") as f:
                f.write(res.text)
    except requests.exceptions.Timeout:
        print("Query Timed Out!")

if __name__ == "__main__":
    test_pipeline()
