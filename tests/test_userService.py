import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock

# Add src directory to path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from userService import register, authenticate, UserExists
from enums import UserType


class TestUserService:
    """Test cases for userService module"""
    
    @patch('userService.userCollection')
    def test_register_new_user(self, mock_collection):
        """Test registering a new user successfully"""
        # Mock the collection methods
        mock_collection.find_one.return_value = None  # User doesn't exist
        mock_collection.insert_one.return_value = Mock()
        
        # Test registration
        register("newuser", "password123")
        
        # Verify insert_one was called with correct data structure
        mock_collection.insert_one.assert_called_once()
        call_args = mock_collection.insert_one.call_args[0][0]
        
        assert call_args["username"] == "newuser"
        assert call_args["userType"] == UserType.User
        assert call_args["isActive"] == True
        assert call_args["chagnePassword"] == False
        assert "salt" in call_args
        assert "password" in call_args
    
    @patch('userService.userCollection')
    @patch('userService.UserExists')
    def test_register_existing_user(self, mock_user_exists, mock_collection):
        """Test registering an existing user"""
        # Mock user exists
        mock_user_exists.return_value = True
        
        # Should not call insert_one
        register("existinguser", "password123")
        mock_collection.insert_one.assert_not_called()
    
    @patch('userService.userCollection')
    def test_authenticate_success(self, mock_collection):
        """Test successful authentication"""
        # Mock user data
        mock_user = {
            "username": "testuser",
            "salt": b"$2b$12$test",
            "password": b"$2b$12$test$hashedpassword"
        }
        mock_collection.find_one.return_value = mock_user
        
        # Mock bcrypt.checkpw to return True
        with patch('userService.bcrypt.checkpw', return_value=True):
            result = authenticate("testuser", "correctpassword")
            assert result == True
    
    @patch('userService.userCollection')
    def test_authenticate_wrong_password(self, mock_collection):
        """Test authentication with wrong password"""
        mock_user = {
            "username": "testuser",
            "salt": b"$2b$12$test",
            "password": b"$2b$12$test$hashedpassword"
        }
        mock_collection.find_one.return_value = mock_user
        
        # Mock bcrypt.checkpw to return False
        with patch('userService.bcrypt.checkpw', return_value=False):
            result = authenticate("testuser", "wrongpassword")
            assert result == False
    
    @patch('userService.userCollection')
    def test_authenticate_user_not_found(self, mock_collection):
        """Test authentication for non-existent user"""
        mock_collection.find_one.return_value = None
        
        result = authenticate("nonexistent", "password")
        assert result == False
    
    @patch('userService.userCollection')
    def test_user_exists_true(self, mock_collection):
        """Test UserExists when user exists"""
        mock_collection.find_one.return_value = {"username": "testuser"}
        
        result = UserExists("testuser")
        assert result == True
    
    @patch('userService.userCollection')
    def test_user_exists_false(self, mock_collection):
        """Test UserExists when user doesn't exist"""
        mock_collection.find_one.return_value = None
        
        result = UserExists("nonexistent")
        assert result == False
