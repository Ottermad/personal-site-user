"""Models file."""
from app import db
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Model):
    """User model."""

    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=True)
    last_name = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=True)
    password_hash = db.Column(db.LargeBinary(), nullable=True)

    def __init__(self, first_name=None, last_name=None, email=None, password=None):
        """Create User object and hash password."""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if password:
            self.password_hash = self.generate_password_hash(password)

    def generate_password_hash(self, password):
        """Generate a password hash."""
        hash = generate_password_hash(password)
        return hash

    def check_password(self, password):
        """Return True if password correct."""
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        """Convert User object to dictionary."""
        return {
            'id': self.pk,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
        }
