from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
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
        
class ToDoForm(FlaskForm):
    to_do_item = StringField("Item :", validators=[InputRequired(message:="You forgot your To Do name")])
    is_complete = BooleanField("Completed", default="unchecked", false_values=None)
    note = TextAreaField("Notes: ")
    Add = SubmitField("Add")