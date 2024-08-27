from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, ValidationError
from models import User


class RegisterForm(FlaskForm):

    username = StringField("Username :", validators = [InputRequired(message:="username must be entered") ], render_kw={"class":"form-control"})
    password = PasswordField("Password : ", validators= [InputRequired(message:="password must be provided")], render_kw={"class":"form-control"})
    submit = SubmitField("Register", render_kw={"class":"btn btn-primary"})

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user != None:
            raise ValidationError("Username Exist")
        
    # def __init__(self, *args, **kwargs):
    #     super(RegisterForm, self).__init__(*args, **kwargs)
    #     self.username.label.class_="form-label"
    #     self.username.class_="form-control"
    #     self.password.label.class_="form-label"
    #     self.password.class_="form-control"
    #     self.submit.class_="btn btn-primary"

        
class ToDoForm(FlaskForm):
    to_do_item = StringField("Item :", validators=[InputRequired(message:="You forgot your To Do name")])
    is_complete = BooleanField("Completed", default="unchecked", false_values=None)
    note = TextAreaField("Notes: ")
    Add = SubmitField("Add")