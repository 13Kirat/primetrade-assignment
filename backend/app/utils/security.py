"""
Security Utilities
"""
import hashlib
import secrets
from jose import jwt
from datetime import datetime, timedelta
from app.config import get_settings

settings = get_settings()

def hash_password(password: str) -> str:
    """
    Hash a password using SHA-256 with a random salt.
    Format: salt$hash
    """
    # Generate a random salt
    salt = secrets.token_hex(32)
    
    # Create hash with salt
    pwd_hash = hashlib.sha256((salt + password).encode('utf-8')).hexdigest()
    
    # Return salt and hash combined
    return f"{salt}${pwd_hash}"

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against its hash.
    """
    try:
        # Split salt and hash
        salt, pwd_hash = hashed_password.split('$')
        
        # Hash the provided password with the stored salt
        new_hash = hashlib.sha256((salt + plain_password).encode('utf-8')).hexdigest()
        
        # Compare hashes
        return new_hash == pwd_hash
    except (ValueError, AttributeError):
        return False

def create_access_token(data: dict) -> str:
    """
    Create JWT access token
    
    Args:
        data: Dictionary containing user data (sub, role, etc.)
    
    Returns:
        Encoded JWT token
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt
