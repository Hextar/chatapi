from main import DB
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, DB.Model):
    """
        Define User model
    """
    id = DB.Column(DB.Integer, primary_key=True)
    first_name = DB.Column(DB.String, nullable=False, unique=False)
    last_name = DB.Column(DB.String, nullable=False, unique=False)
    email = DB.Column(DB.String(40), unique=True, nullable=False)
    password = DB.Column(DB.String(200), primary_key=False, unique=False, nullable=False)

    rooms = relationship("Room", secondary="ChatRoom")

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)