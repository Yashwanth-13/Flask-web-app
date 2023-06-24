from flask import Flask, request, render_template



app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/registration', methods=["GET", "POST"])
def registration():
    return render_template("registration.html")
