from database.db_manager import DatabaseManager
from models.user import User


class AuthService:
    """
    Handles registration and login logic.
    """

    def __init__(self):
        self.db = DatabaseManager()

    def register(self, name, email, password, role):
        password_hash = User.hash_password(password)
        self.db.create_user(name, email, password_hash, role)

    def login(self, email, password):
        user = self.db.get_user_by_email(email)
        if not user:
            return None

        password_hash = User.hash_password(password)

        if user[3] == password_hash:
            return user
        return None