from config import app, db

from routes import *
with app.app_context():
    db.create_all()


app.run(debug=True, host="0.0.0.0", port=5001)