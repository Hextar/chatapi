from flask import render_template, request
from flask_login import login_required, current_user

from main import APP

@APP.route("/chat", methods=['POST', 'GET'])
@login_required
def chat():
    """
        Render the chat view
    """

    from app.models.user import User
    from app.models.room import Room
    from app.models.message import Message

    default_room = Room.query.all()[0]
    messages = Message.query.filter_by(
        room=default_room).order_by(-Message.posted_at).limit(50).all()
    print('************')
    print(messages)

    for msg in messages:
        print(msg.data, msg.posted_at)

    return render_template('chat.html', messages=messages)