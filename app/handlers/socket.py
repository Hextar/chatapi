import pika

from main import APP, socketio

from flask import render_template
from flask_login import current_user
from flask_socketio import send, emit

from app.channel.room import RabbitRoom
from app.bot.service import BotService


@socketio.on('connect')
def message():
    """
        Render home view
    """
    
    pass

@socketio.on('message')
def message(msg):
    """
        Listen incoming messages from a client
        Also indentify the stock intent to send back a quote as an answer from the Bot

        parameter:
            msg: {
                room: '',
                data: '',
                sender: ''
            }
    """
    from app.models.message import Message
    from app.models.room import Room
    from app.models.user import User

    from main import DB

    stock_code = None
    data = msg.get('data')
    sender = current_user.email
    msg['sender'] = sender

    available_rooms = Room.query.all()
    if len(available_rooms) > 0:
        room = available_rooms[0]
    else:
        # create default room
        room = Room(title='Default Room')
        DB.session.add(room)
        DB.session.commit()

    user = User.query.filter_by(email=current_user.email).first()
    if user and room:
        message = Message(data=data, room=room, user=user)
        DB.session.add(message)
        DB.session.commit()

    if '/stock=' in data:
        stock = data.split('=')
        stock_code = stock[1]
        quote = BotService().quote_stock(stock_code)

        if quote != -1 and quote != 'N/D':
            data = '{stock_code} quote is ${quote} per share'.format(
                stock_code=stock_code.upper(),
                quote=quote
            )
            msg = {
                'data': data,
                'sender': 'StockBot'
            }
        else:
            msg = {
                'data': 'Sorry I could not find a quote for stock code: %s' % stock_code,
                'sender': 'StockBot'
            }
    

            
    send(msg, broadcast=True)


