from main import DB

class Room(DB.Model):
    """Model Room"""

    id = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String(300))