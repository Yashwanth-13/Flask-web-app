from flask import Flask, request, render_template
import sqlite3

db = sqlite3.connect("databases/info.db")

cursor = db.cursor()

target_fish_name = "Jamie"
rows = cursor.execute("SELECT name, species, tank_number FROM fish WHERE name = ?",(target_fish_name,),).fetchall()
print(rows)



app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        
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
