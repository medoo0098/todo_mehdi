from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80) , unique=False, nullable=False)


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    to_do_item = db.Column(db.String(80), unique=False, nullable=False)
    is_complete = db.Column(db.Boolean, default=False)
    note = db.Column(db.String(400), nullable=True, unique=False)


