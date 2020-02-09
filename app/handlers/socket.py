import pika

from main import APP, socketio

from flask import render_template
from flask_socketio import send, emit

from app.channel.room import RabbitRoom
from app.bot.service import BotService


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
    stock_code = None
    data = msg.get('data')

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
                'data': data
            }
    send(msg, broadcast=True)


