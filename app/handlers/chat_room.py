from flask import render_template

from main import APP, socketio

@APP.route("/rooms/<room_id>")
def chat_room(room_id):
    """
        Render home view
    """
    
    print('************************************************')

    return render_template('chat_room.html', room=room_id)