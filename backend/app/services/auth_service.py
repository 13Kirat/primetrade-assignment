"""
Authentication Service
"""
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserLogin, TokenResponse
from app.utils.security import hash_password, verify_password, create_access_token

class AuthService:
    def __init__(self, db: Session):
        self.db = db
    
    def register_user(self, user_data: UserCreate) -> dict:
        """Register a new user and return user with token"""
        # Check if user already exists
        existing_user = self.db.query(User).filter(User.email == user_data.email).first()
        if existing_user:
            raise ValueError("Email already registered")
        
        # Create new user
        hashed_password = hash_password(user_data.password)
        new_user = User(
            name=user_data.name,
            email=user_data.email,
            password_hash=hashed_password,
            role="user"
        )
        
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        
        # Create access token for auto-login
        access_token = create_access_token(data={"sub": str(new_user.id), "role": new_user.role})
        
        return {
            "user": new_user,
            "access_token": access_token,
            "token_type": "bearer"
        }
    
    def login_user(self, credentials: UserLogin) -> TokenResponse:
        """Authenticate user and return JWT token"""
        user = self.db.query(User).filter(User.email == credentials.email).first()
        
        if not user:
            raise ValueError("Invalid email or password")
        
        if not user.is_active:
            raise ValueError("Account is inactive")
        
        if not verify_password(credentials.password, user.password_hash):
            raise ValueError("Invalid email or password")
        
        # Create access token
        access_token = create_access_token(data={"sub": str(user.id), "role": user.role})
        
        return TokenResponse(access_token=access_token, token_type="bearer")
