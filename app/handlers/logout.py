from main import APP

from flask import redirect, url_for
from flask_login import logout_user, login_required

@APP.route("/logout")
@login_required
def logout():
    """Logout."""

    logout_user()
    return redirect(url_for('signin'))