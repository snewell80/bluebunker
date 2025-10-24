import pytest
import sys
import os
from unittest.mock import patch

# Add src directory to path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from config import client, db, userCollection


class TestConfig:
    """Test cases for config module"""
    
    def test_client_connection(self):
        """Test that MongoDB client is properly configured"""
        assert client is not None
        # Check that the client has the expected connection string
        assert str(client.address) == "('localhost', 27017)"
    
    def test_database_name(self):
        """Test that database name is correct"""
        assert db.name == 'Blue-Bunker'
    
    def test_user_collection(self):
        """Test that user collection is properly configured"""
        assert userCollection is not None
        assert userCollection.name == 'users'
        assert userCollection.database == db
