from datetime import datetime

from main import DB
from .room import Room
from .user import User

class Message(DB.Model):
    """Model Message"""

    id = DB.Column(DB.Integer, primary_key=True)
    data = DB.Column(DB.String(1000))
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable=False)
    room_id = DB.Column(DB.Integer, DB.ForeignKey('room.id'), nullable=False) 
    user = DB.relationship('User')
    room = DB.relationship('Room')
    posted_at = DB.Column(DB.DateTime, nullable=False, default=datetime.utcnow)
