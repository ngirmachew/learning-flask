from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField

class SignupForm(Form):
    first_name = StringField('First name')
    last_name = StringField('Last name')
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Sign up')