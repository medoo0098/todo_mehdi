from dotenv import load_dotenv
import os
import pandas as pd
from flask import Flask, render_template, redirect, url_for, flash, current_app, request, send_file, send_from_directory


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


    # """
    # Renders the index.html template and returns it as the response for the root URL ("/").

    # Returns:
    #     The rendered index.html template.
    # """


@app.route('/')
def index():
    return render_template('index.html')




app.run(debug=True, host="0.0.0.0", port=5001)

