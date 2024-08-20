from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import *



def create_app():
    app = Flask(__name__)
    app.comfig.from_object(Config)
    db = SQLAlchemy()
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
    

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)