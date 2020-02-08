from main import DB

class Room(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String, nullable=False, unique=False)

    user = relationship("ChatRoom", back_populates="rooms")