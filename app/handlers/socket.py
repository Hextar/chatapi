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
    stock_code = None
    data = msg.get('data')
    sender = current_user.email
    msg['sender'] = sender


    if '/stock=' in data:
        stock = data.split('=')
        stock_code = stock[1]
        quote = BotService().quote_stock('aapl.us')
        if quote != -1:
            data = '{stock_code} quote is ${quote} per share'.format(
                stock_code=stock_code.upper(),
                quote=quote
            )
            msg = {
                'data': data,
                'sender': 'StockBot'
            }
    send(msg, broadcast=True)


