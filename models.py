from config import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(512) , unique=False, nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    to_do_item = db.Column(db.String(80), unique=False, nullable=False)
    is_complete = db.Column(db.Boolean, default=False)
    note = db.Column(db.String(400), nullable=True, unique=False)
    time = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"),nullable=False)


