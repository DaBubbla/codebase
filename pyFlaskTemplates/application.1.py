import os

from flask import Flask, render_template, request
from tempfile import mkdtemp

from werkzeug.security import check_password_hash, generate_password_hash

# from helpers import ...

# Configure Application
app = Flask(__name__)

# Enable debugging
app.config["FLASK_ENV"] = 'development'

# Enable auto-reload on templates
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Don't cache responses
@app.after_request
def after_response(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers['Expires'] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# # Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_FILE_DIR"] = mkdtemp()
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = 'filesystem'
# Session(app)

@app.route("/")
def index():
    # return "hello world" Its alive!
    return render_template("index.html")

@app.route("/area1", methods=["GET", "POST"])
def area1():
    if request.method == "POST":
        return "Error: This is area - 1. Method == POST"
    else:
        return "This is area - 1. Method != POST"

@app.route("/area2", methods=["GET", "POST"])
def area2():
    if request.method == "POST":
        return "Error: This is area - 2. Method == POST"
    else:
        return "This is area - 2. Method != POST"