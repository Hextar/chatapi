from main import DB

from sqlalchemy.orm import relationship

class Room(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String, nullable=False, unique=False)

    users = relationship("User", secondary="ChatRoom")