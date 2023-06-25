from flask import Flask, request, render_template
import sqlite3

db = sqlite3.connect("databases/info.db", check_same_thread=False)

cursor = db.cursor()


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        course = request.form.get("course")
        gender  = request.form.get("gender")
        phone = request.form.get("phone")
        if len(phone) != 10:
            return render_template("invalid_register.html", invalid=phone)
        email = request.form.get("email")
        values = ["@", ".com"]
        if values not in email:
            return render_template("invalid_register.html", invalid=email)
        

@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_name = request.form.get("username")
        pass_word = request.form.get("password")
        user_id = cursor.execute("SELECT id FROM credentials WHERE username = ? AND password = ?", (user_name, pass_word,),).fetchall()
        if user_id:
            first_name, last_name = cursor.execute("SELECT first_name, last_name FROM data WHERE data_id = ?", (user_id[0]),).fetchall()
            return render_template("home.html", first_name=first_name, last_name=last_name)
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
