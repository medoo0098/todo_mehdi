from config import app
from flask import render_template, request, url_for

@app.route('/')
def index():
    return render_template('index.html', title="TODO")


@app.route('/login', methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        print(f" username = {username} , password = {password}")

    return render_template('login.html', title="Login")

