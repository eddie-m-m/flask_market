from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email_address = StringField(label='email')
    password1 = PasswordField(label='password1')
    password2 = PasswordField(label='password2')
    submit = SubmitField(label='submit')

