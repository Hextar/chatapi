from main import DB


class ChatRoom(DB.Model):
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    room_id = Column(Integer, ForeignKey('room.id'), primary_key=True)
    child = relationship("User", back_populates="users")
    parent = relationship("Room", back_populates="rooms")
