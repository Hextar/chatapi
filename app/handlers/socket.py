import pika

from main import APP, socketio

from flask import render_template
from flask_socketio import send, emit

from app.channel.room import RabbitRoom


@socketio.on('connect')
def message():
    """
        Render home view
    """
    
    print('************************************************')

@socketio.on('message')
def message(msg):
    """
        Render home view
    """
    send(msg, broadcast=True)


