from backend.auth_utils import get_password_hash, verify_password

try:
    print("Testing Password Hashing...")
    pwd = "testpassword"
    hashed = get_password_hash(pwd)
    print(f"Hash: {hashed}")
    
    print("Testing Password Verification...")
    is_valid = verify_password(pwd, hashed)
    print(f"Verification: {is_valid}")
    
    if is_valid:
        print("AUTH UTILS SUCCESS")
    else:
        print("AUTH UTILS FAILED")

except Exception as e:
    print(f"AUTH UTILS CRASHED: {e}")
