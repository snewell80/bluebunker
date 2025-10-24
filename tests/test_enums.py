import pytest
import sys
import os

# Add src directory to path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from enums import UserType


class TestEnums:
    """Test cases for enums module"""
    
    def test_user_type_values(self):
        """Test that UserType enum has correct values"""
        assert UserType.SuperUser == 1
        assert UserType.User == 2
        assert UserType.Watcher == 3
    
    def test_user_type_enum_properties(self):
        """Test UserType enum properties"""
        assert isinstance(UserType.SuperUser, int)
        assert isinstance(UserType.User, int)
        assert isinstance(UserType.Watcher, int)
    
    def test_user_type_iteration(self):
        """Test that we can iterate over UserType enum"""
        user_types = list(UserType)
        assert len(user_types) == 3
        assert UserType.SuperUser in user_types
        assert UserType.User in user_types
        assert UserType.Watcher in user_types
