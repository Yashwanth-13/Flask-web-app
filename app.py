from flask import Flask, request, render_template
import sqlite3

db = sqlite3.connect("databases/info.db")

cursor = db.cursor()


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_id = cursor.execute("SELECT id FROM credentials WHERE username = ? AND password = ?", (username, password),).fetchall()
        if user_id:
            first_name, last_name = cursor.execute("SELECT first_name, last_name FROM data WHERE data_id = ?", (int(user_id),),).fetchall()
            return render_template("home.html", {{ first_name }}, {{ last_name }})
        else:
            return render_template("invalid_login.html")
    

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/registration', methods=["GET", "POST"])
def registration():
    return render_template("registration.html")
