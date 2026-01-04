import requests

print("Triggering Query...")
try:
    res = requests.post(
        "http://127.0.0.1:8000/api/v1/query/submit",
        data={"input_type": "TEXT", "original_input": "test"},
    )
    print(f"Status: {res.status_code}")
    print(f"Text: {res.text}")
except Exception as e:
    print(f"Request Failed: {e}")
