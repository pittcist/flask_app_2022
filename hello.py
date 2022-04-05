from flask import Flask, request, redirect, url_for, render_template
import sqlite3 as sql
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/<int:score>")
def hello_world(score):
    # return "Hello <b>World</b>!"
    return render_template("login.htm", score=score)

@app.route("/hello/<float:studentID>/")
def hello(studentID):
    return "Hello {0}".format(studentID)

@app.route("/success/<name>")
def success(name):
    return "Welcome {0}!".format(name)

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["nm"]
        return redirect(url_for("success", name=username))

@app.route("/student")
def student():
    return render_template("student.htm")

@app.route("/addrec/", methods = ["POST", "GET"])
def addrec():
    if request.method == "POST":
        nm = request.form["nm"]
        addr = request.form["addr"]
        city = request.form["city"]
        pin = request.form["pin"]
    
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO students (name, address, city, pin) VALUES ('{0}', '{1}', '{2}', '{3}')".format(nm, addr, city, pin))
        con.commit()
        message = "Student record added successfully"

    return render_template("result.htm", msg = message)

@app.route("/list/")
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row 

    cur = con.cursor()
    cur.execute("SELECT * FROM students")

    rows = cur.fetchall()
    return render_template("list.htm", rows = rows)

if __name__ == "__main__":
    app.run(debug=True)
    