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
        gender  = request.form.get("Gender")
        phone = request.form.get("phone")
        if len(phone) != 10:
            return "<p>Invalid Phone number!</p>"
        email = request.form.get("email")
        values = ["@", ".com"]
        if not (values[0] in email and values[1] in email):
            return "<p>Invalid Email!</p>"
        username = request.form.get("username")
        password = request.form.get("password")
        reTypedPassword = request.form.get("re-typed")
        if password != reTypedPassword:
            return "<p>Passwords do not match!</p>"
        cursor.execute("INSERT INTO credentials (username, password) VALUES (?, ?)", (username, password,))
        cursor.execute("INSERT INTO data (data_id, first_name, last_name, gender, phone, mail, course) VALUES ((SELECT id FROM credentials WHERE username = ?), ?, ?, ?, ?, ?, ?)", (username, firstname, lastname, gender, phone, email, course,))
        db.commit()
        return render_template("login.html")
        

@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_name = request.form.get("username")
        pass_word = request.form.get("password")
        user_id = cursor.execute("SELECT id FROM credentials WHERE username = ? AND password = ?", (user_name, pass_word,),).fetchall()
        user_id = user_id[0][0]
        if user_id:
            the_names = cursor.execute("SELECT first_name, last_name FROM data WHERE data_id = ?", (user_id,),).fetchall()
            first_name = the_names[0][0]
            last_name = the_names[0][1]
            user_db = sqlite3.connect("databases/current_user.db", check_same_thread=False)
            user_cursor = user_db.cursor()
            user_cursor.execute("INSERT INTO current_user (first_name, last_name) VALUES (?, ?)", (first_name, last_name,))
            user_db.commit()
            return render_template("home.html", first_name=first_name, last_name=last_name)
        else:
            return render_template("invalid_login.html")
    else:
        user_db = sqlite3.connect("databases/current_user.db", check_same_thread=False)
        user_cursor = user_db.cursor()
        names = user_cursor.execute("SELECT first_name, last_name FROM current_user").fetchall()
        first_name = names[0][0]
        last_name = names[0][1]
        return render_template("home.html", first_name=first_name, last_name=last_name)
    

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/registration', methods=["GET", "POST"])
def registration():
    return render_template("registration.html")
