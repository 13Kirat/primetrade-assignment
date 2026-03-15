"""
Authentication Routes
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse, TokenResponse
from app.services.auth_service import AuthService
from app.dependencies.auth_dependency import get_current_user
from app.models.user import User
from app.utils.response import success_response, error_response
from app.utils.logger import setup_logger

logger = setup_logger(__name__)
router = APIRouter()

@router.post("/register", response_model=dict, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user and automatically log them in
    
    - **name**: User's full name
    - **email**: Valid email address
    - **password**: Minimum 6 characters
    
    Returns user info and JWT token for immediate login
    """
    try:
        auth_service = AuthService(db)
        result = auth_service.register_user(user_data)
        logger.info(f"User registered and logged in: {result['user'].email}")
        return success_response(
            data={
                "user": UserResponse.model_validate(result['user']),
                "access_token": result['access_token'],
                "token_type": result['token_type']
            },
            message="User registered successfully"
        )
    except ValueError as e:
        logger.warning(f"Registration failed: {str(e)}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/login", response_model=dict)
async def login(credentials: UserLogin, db: Session = Depends(get_db)):
    """
    Login and receive JWT access token
    
    - **email**: Registered email
    - **password**: User password
    """
    try:
        auth_service = AuthService(db)
        token = auth_service.login_user(credentials)
        logger.info(f"User logged in: {credentials.email}")
        return success_response(
            data=token,
            message="Login successful"
        )
    except ValueError as e:
        logger.warning(f"Login failed: {str(e)}")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

@router.get("/me", response_model=dict)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    """
    Get current authenticated user information
    
    Requires valid JWT token in Authorization header
    """
    return success_response(
        data={"user": UserResponse.model_validate(current_user)},
        message="User retrieved successfully"
    )
