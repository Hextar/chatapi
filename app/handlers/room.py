from flask import render_template

from main import APP

@APP.route("/rooms")
def rooms():
    """
        Render home view
    """
    
    print('************************************************')

    return render_template('rooms.html')