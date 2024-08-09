from dotenv import load_dotenv
import os
import pandas as pd
from flask import Flask, render_template, redirect, url_for, flash, current_app, request, send_file, send_from_directory
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")



app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL


db = SQLAlchemy()
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)


class To_do(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    to_do_item = db.Column(db.String(80), unique=False, nullable=False)
    is_complete = db.column(db.boolean, default=False)
    note = db.column(db.String(400), nulable=True, unique=False)
    


with app.app_context():
    db.create_all()










@app.route('/')
def index():
    return render_template('index.html')




app.run(debug=True, host="0.0.0.0", port=5001)

