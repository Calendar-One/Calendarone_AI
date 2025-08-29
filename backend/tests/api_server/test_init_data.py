import pytest
from sqlalchemy.orm import Session
from api_server.models.users import User


sample_user_data = {
    "user_name": "user1",
    "email": "user1@example.com",
    "password": "password1"
}

sample_user_data_2 = {
    "user_name": "user2",
    "email": "user2@example.com",
    "password": "password2"
}

class TestUserCRUD:
    """Test class for User model CRUD operations."""

    def test_create_user(self, test_db_session: Session):
        """Test creating a new user."""
        # Create user
        user = User(**sample_user_data)
        test_db_session.add(user)
        test_db_session.commit()
        test_db_session.refresh(user)

        # Assertions"]
        assert user.user_name == sample_user_data["user_name"]
        assert user.email == sample_user_data["email"]
        assert user.password == sample_user_data["password"]
        assert user.is_deleted is False
        assert user.created_at is not None
        assert user.updated_at is not None
        assert user.deleted_at is None

    def test_read_user(self, test_db_session: Session):
        """Test reading a user from database."""
        # Create user first
        user = User(**sample_user_data_2)
        test_db_session.add(user)
        test_db_session.commit()

        # Read user
        retrieved_user = test_db_session.query(User).filter(
            User.email == sample_user_data_2["email"]
        ).first()

        # Assertions
        assert retrieved_user is not None
        assert retrieved_user.user_name == sample_user_data_2["user_name"]
        assert retrieved_user.email == sample_user_data_2["email"]

    def test_update_user(self, test_db_session: Session):
        """Test updating a user."""
      
         # Read user
        user = test_db_session.query(User).filter(
            User.email == sample_user_data_2["email"]
        ).first()

        # Store original updated_at
        original_updated_at = user.updated_at

        # Update user
        new_user_name = "updated_user"
        new_email = "updated@example.com"
        
        user.user_name = new_user_name
        user.email = new_email
        test_db_session.commit()
        test_db_session.refresh(user)

        # Assertions
        assert user.user_name == new_user_name
        assert user.email == new_email
        assert user.updated_at > original_updated_at  # updated_at should be updated



    def test_create_multiple_users(self, db_session: Session):
        """Test creating multiple users."""
        users_data = [
            {
                "user_name": "user1",
                "email": "user1@example.com",
                "password": "password1"
            },
            {
                "user_name": "user2",
                "email": "user2@example.com",
                "password": "password2"
            },
            {
                "user_name": "user3",
                "email": "user3@example.com",
                "password": "password3"
            }
        ]

        # Create users
        users = []
        for user_data in users_data:
            user = User(**user_data)
            db_session.add(user)
            users.append(user)
        
        db_session.commit()

        # Verify all users were created
        for user_data in users_data:
            retrieved_user = db_session.query(User).filter(
                User.email == user_data["email"]
            ).first()
            assert retrieved_user is not None
            assert retrieved_user.email == user_data["email"]

        # Verify total count
        total_users = db_session.query(User).count()
        assert total_users == 3