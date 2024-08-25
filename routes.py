from flask import render_template, request, url_for, redirect
from models import User, ToDo
from forms import RegisterForm, ToDoForm
from config import db
from werkzeug.security import generate_password_hash, check_password_hash 

from flask_login import LoginManager, login_user, current_user, logout_user, login_required


def init_routes(app):

    login_manager = LoginManager(app)
    login_manager.login_view = "login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    @app.route('/', methods=["GET","POST"])
    def index():
        form = ToDoForm()
        if form.validate_on_submit():
            new_todo = ToDo(
                to_do_item = form.to_do_item.data,
                is_complete = form.is_complete.data,
                note = form.note.data
            )
            db.session.add(new_todo)
            db.session.commit()
            return redirect(url_for("index"))
            
        list_items = ToDo.query.all()
        for item in list_items:
            print(item.to_do_item)


        if current_user:
            
            return render_template('index.html', title="TODO", form=form, list_items=list_items, current_user=current_user)
        else:
            return render_template('index.html', title="TODO", form=form, list_items=list_items)


    @app.route('/login', methods=("GET", "POST"))
    def login():
        if current_user.is_authenticated:
            return redirect(url_for("index"))
        
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            user = User.query.filter_by(username = username).first()
            if user and check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for("index"))

            

            print(user.username)
            

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