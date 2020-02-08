from datetime import datetime

from main import DB
from sqlalchemy.orm import relationship


class ChatRoom(DB.Model):
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), primary_key=True)
    room_id = DB.Column(DB.Integer, DB.ForeignKey('room.id'), primary_key=True)
    message = DB.Column(DB.String, nullable=False, unique=False, default='')
    date = DB.Column(DB.DateTime, onupdate=datetime.now) 

    child = relationship("User", back_populates="users")
    parent = relationship("Room", back_populates="rooms")
