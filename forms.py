from wtforms import StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, ValidationError
from models import User


class RegisterForm(FlaskForm):

    username = StringField("Username :", validators = [InputRequired(message:="username must be entered")])
    password = PasswordField("Password : ", validators= [InputRequired(message:="password must be provided")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user != None:
            raise ValidationError("Username Exist")
        
