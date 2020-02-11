from flask import render_template, request
from flask_login import login_required

from main import APP

@APP.route("/chat", methods=['POST'])
@login_required
def chat():
    """
        Render the chat view
    """
    return render_template('chat.html')