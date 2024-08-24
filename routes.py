from flask import render_template, request, url_for, redirect
from models import User
from forms import RegisterForm
from config import db


def init_routes(app):

    @app.route('/')
    def index():
        return render_template('index.html', title="TODO")


    @app.route('/login', methods=("GET", "POST"))
    def login():
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]

            user = User.query.filter_by(username = username).first()

            print(user.username)
            

            # print(f" username = {username} , password = {password}")

        return render_template('login.html', title="Login")

    @app.route("/register", methods= ("GET", "POST"))
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            new_user =  User(
                username = form.username.data,
                password = form.password.data
                            )
            db.session.add(new_user)
            db.session.commit()
            print("user created")
            return redirect(url_for("login"))
        else: 
            if form.errors:
                print(form.errors)
            errors = form.errors.values()        
        return render_template("register.html", form=form, title="register", errors=errors)