"""
Standardized API Response Utilities
"""
from typing import Any, Optional

def success_response(data: Optional[Any] = None, message: str = "Success") -> dict:
    """
    Create a standardized success response
    
    Args:
        data: Response data
        message: Success message
    
    Returns:
        Standardized response dictionary
    """
    response = {
        "success": True,
        "message": message
    }
    if data is not None:
        response["data"] = data
    return response

def error_response(message: str, details: Optional[Any] = None) -> dict:
    """
    Create a standardized error response
    
    Args:
        message: Error message
        details: Additional error details
    
    Returns:
        Standardized error response dictionary
    """
    response = {
        "success": False,
        "message": message
    }
    if details is not None:
        response["details"] = details
    return response
