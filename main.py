from config import app, db
from flask import render_template

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True, host="0.0.0.0", port=5001)