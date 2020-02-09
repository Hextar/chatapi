import json
import logging

from main import APP
from app.session.user import User

from flask import redirect, make_response, render_template, url_for
from flask_login import login_user

from app.forms.signin import SigninEmailForm

@APP.route('/', methods=['GET', 'POST'])
def signin():
    """Signin"""
    form = SigninEmailForm()

    if form.validate_on_submit():
        user = User(form.email.data, form.email.data)
        login_user(user, remember=True)

        
        return make_response(redirect(url_for('chat')))

    return render_template(
        'signin.html', form=form)
