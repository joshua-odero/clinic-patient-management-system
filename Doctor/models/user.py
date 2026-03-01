import hashlib


class User:
    """
    Base User class.
    Parent class for Admin, Doctor, Receptionist.
    Demonstrates encapsulation and inheritance.
    """

    def __init__(self, user_id, name, email, password_hash, role):
        self._id = user_id
        self._name = name
        self._email = email
        self._password_hash = password_hash
        self._role = role

    # ----------- PROPERTIES (Encapsulation) -----------

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def role(self):
        return self._role

    # ----------- STATIC METHOD -----------

    @staticmethod
    def hash_password(password):
        """Hashes password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()