from typing import Optional
from api_server.core.security import verify_password
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


user_service = UserService(model=User)
