from flask import render_template, request, url_for, redirect, session, flash
from models import User, ToDo
from forms import RegisterForm, ToDoForm
from config import db
from werkzeug.security import generate_password_hash, check_password_hash 
from datetime import datetime

from flask_login import LoginManager, login_user, current_user, logout_user, login_required


def init_routes(app):

    login_manager = LoginManager(app)
    login_manager.login_view = "login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    @app.route('/', methods=["GET","POST"])
    @login_required
    def index():

        
            
        list_items = list(ToDo.query.filter_by(user_id=current_user.id))
        list_items = sorted(list_items, key=lambda x: x.time)
        if len(list_items)<1:
            print("No items added")
        else:

            for item in list_items:
                print(item.to_do_item)

        return render_template('index.html', title="TODO", list_items=list_items)


    @app.route("/edit/<int:todo_id>", methods=["GET"])
    @login_required
    def edit(todo_id):
        todo=ToDo.query.filter_by(id=todo_id).first_or_404()
        print(f"        items is {todo.is_complete}")
        todo.is_complete = not todo.is_complete
        db.session.commit()
        print(f"        items is {todo.is_complete}")
        return redirect(url_for("index"))


    @app.route("/add_task", methods=["GET", "POST"])
    @login_required
    def add_task():

        form = ToDoForm()
        if form.validate_on_submit():
            new_todo = ToDo(
                to_do_item = form.to_do_item.data,
                is_complete = form.is_complete.data,
                note = form.note.data,
                time = datetime.now(),
                user_id = current_user.id
            )
            db.session.add(new_todo)
            db.session.commit()
            flash(f"Task added successfully", "success")
            return redirect(url_for("index"))
        else:
            flash(f"Something went wrong", "danger")

        return render_template("add-item.html", form=form, title="Add new task")



    @app.route("/delete/<int:todo_id>", methods=["GET"])
    @login_required
    def delete(todo_id):
        todo = ToDo.query.filter_by(id=todo_id).first_or_404()
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for("index"))
    

    

    @app.route('/login', methods=("GET", "POST"))
    def login():
        if current_user.is_authenticated:
            flash(f"user {current_user.username} is loggedin.", "success")
            return redirect(url_for("index"))
        
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            user = User.query.filter_by(username = username).first()
            if user and check_password_hash(user.password, password):
                login_user(user, remember=True)
                flash(f"user {current_user.username} is loggedin.", "success")
                return redirect(url_for("index"))
            else:
                flash(f"incorrect username or password", "danger")

            
            

            # print(f" username = {username} , password = {password}")

        return render_template('login.html', title="Login")

    @app.route("/register", methods= ("GET", "POST"))
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            new_user =  User(
                username = form.username.data,
                password = generate_password_hash(f"{form.password.data}", method="pbkdf2:sha256", salt_length=8)
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
    

    @app.route("/aboute")
    def about():
        return render_template("about.html", title="About")
    

    @app.route("/logout")
    def logout():
        # session.pop(current_user, None)
        user = current_user.username
        logout_user()
        flash(f"user {user.capitalize()} is logged out.", "warning")
        return redirect(url_for("login"))