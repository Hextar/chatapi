import logging

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, ValidationError, Length
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField, StringField

class SigninEmailForm(FlaskForm):
    email = EmailField('Your Email', [DataRequired(), Email()])
    password = PasswordField('Password', [Length(min=6, max=35)])