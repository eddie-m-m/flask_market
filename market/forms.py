from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='User Name:')
    email_address = StringField(label='Email Address:')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Confirm Password')
    submit = SubmitField(label='Create Account')

