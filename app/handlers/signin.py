import json
import logging

from main import APP, DB
from app.session.user import User

from flask import redirect, make_response, render_template, url_for
from flask_login import login_user

from app.forms.signin import SigninEmailForm

@APP.route('/', methods=['GET', 'POST'])
def signin():
    """Signin"""
    form = SigninEmailForm()
    from app.models.user import User as UserModel

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User(email, email)

        new_user = UserModel.query.filter_by(email=email).first()
        if new_user is None:
            new_user = UserModel(email=email)
            new_user.set_password(password)
            DB.session.add(new_user)
            DB.session.commit()

        if new_user.check_password(password) is False:
            form.password.errors.append('Wrong password or you forgot it.')
            return render_template('signin.html', form=form)
            

        login_user(user, remember=True)

        resp = make_response(redirect(url_for('chat')))
        
        return resp

    return render_template(
        'signin.html', form=form)
