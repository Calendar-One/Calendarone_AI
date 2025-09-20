from typing import Optional
from api_server.core.security import verify_password, create_refresh_token, verify_refresh_token, get_refresh_token_expiration, is_refresh_token_expired
from api_server.models.users import User
from api_server.services.base import BaseService
from sqlalchemy.orm import Session


class UserService(BaseService):
    def get_user_by_email(
        self,
        session: Session,
        email: str,
    ) -> User:
        """
        Get a user by email.
        """
        return session.query(User).filter(User.email == email).first()

    def authenticate_user(
        self, db: Session, email: str, password: str
    ) -> Optional[User]:
        """
        Authenticates a user with the given email and password.

        Parameters:
            db (Session): The database session object.
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            Optional[User]: The authenticated user if successful, None otherwise.
        """
        user = self.get_user_by_email(db, email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def generate_and_save_refresh_token(self, db: Session, user: User) -> str:
        """
        Generate a new refresh token and save it to the user.

        Parameters:
            db (Session): The database session object.
            user (User): The user to generate refresh token for.

        Returns:
            str: The generated refresh token.
        """
        refresh_token = create_refresh_token()
        user.refresh_token = refresh_token
        user.refresh_token_expires_at = get_refresh_token_expiration()
        db.commit()
        db.refresh(user)
        return refresh_token

    def authenticate_with_refresh_token(
        self, db: Session, refresh_token: str
    ) -> Optional[User]:
        """
        Authenticates a user with a refresh token.

        Parameters:
            db (Session): The database session object.
            refresh_token (str): The refresh token.

        Returns:
            Optional[User]: The authenticated user if successful, None otherwise.
        """
        user = db.query(User).filter(User.refresh_token == refresh_token).first()
        if not user:
            return None
        if not user.is_active:
            return None
        
        # Check if refresh token is expired
        if is_refresh_token_expired(user.refresh_token_expires_at):
            # Clear expired token
            user.refresh_token = None
            user.refresh_token_expires_at = None
            db.commit()
            return None
            
        return user

    def revoke_refresh_token(self, db: Session, user: User) -> None:
        """
        Revoke the user's refresh token.

        Parameters:
            db (Session): The database session object.
            user (User): The user to revoke refresh token for.
        """
        user.refresh_token = None
        user.refresh_token_expires_at = None
        db.commit()
        db.refresh(user)

    def cleanup_expired_refresh_tokens(self, db: Session) -> int:
        """
        Clean up expired refresh tokens from the database.

        Parameters:
            db (Session): The database session object.

        Returns:
            int: The number of expired tokens cleaned up.
        """
        from datetime import datetime, timezone
        current_time = datetime.now(timezone.utc)
        
        expired_users = db.query(User).filter(
            User.refresh_token_expires_at.isnot(None),
            User.refresh_token_expires_at < current_time
        ).all()
        
        count = len(expired_users)
        for user in expired_users:
            user.refresh_token = None
            user.refresh_token_expires_at = None
        
        if count > 0:
            db.commit()
            
        return count


user_service = UserService(model=User)
