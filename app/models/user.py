from main import DB
from werkzeug.security import generate_password_hash, check_password_hash

class User(DB.Model):
    """Model User"""

    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(120), unique=True, nullable=False)
    password_hash = DB.Column(DB.String(128))

    def __repr__(self):
        return '<User %r>' % self.email
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)