from flask import Flask, g, current_app, render_template, request

import sqlite3, math

app = Flask(__name__)

@app.route("/")
def base():
    # render the base.html template
    return render_template("base.html")

def get_info_db():
    # check whether there is a database called info_db
    # in the g attribute of the app
    if 'info_db' not in g:
        # connect to the database
        g.info_db = sqlite3.connect("info_db.sqlite")

    # execute the SQL command in the init.sql file
    with current_app.open_resource('init.sql') as f:
        g.info_db.executescript(f.read().decode('utf8'))

    # return the connection g.info_db
    return g.info_db

def insert_info(request):
    # extract the info from request
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    height = request.form["height"]
    weight = request.form["weight"]
    systolic = request.form["systolic"]
    diastolic = request.form["diastolic"]
    smoke = request.form["smoke"]

    # connect to the database
    db = get_info_db()

    # use a cursor to insert the message into the database
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO info (name, age, gender, height, weight, systolic, diastolic, smoke) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
        (name, age, gender, height, weight, systolic, diastolic, smoke)
    )
    # save the insertion
    db.commit()

    # close the database connection
    db.close()

    return(name, age, gender, height, weight, systolic, diastolic, smoke)

@app.route("/submit/", methods = ["POST", "GET"])
def submit():
    # render the submit.html template in the GET case
    if request.method == "GET":
        return render_template("submit.html")
    # call the insert_info() function 
    # and render the submit.html with parameters
    # in the POST case
    else:
        name, age, gender, height, weight, systolic, diastolic, smoke = insert_info(request)
        return render_template("submit.html", 
                               name=name,
                               age=age, 
                               gender=gender, 
                               height=height,
                               weight=weight, 
                               systolic=systolic, 
                               diastolic=diastolic, 
                               smoke=smoke)

def random_info():
    # connect to the database
    db = get_info_db()

    # use a cursor to select a collection of n random messages
    # from the database
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM info')
    result = cursor.fetchall()

    # close the database connection
    db.close()

    return(result)

@app.route("/result/")
def result():
    info = random_info()
    # render the view.html template with the info as an argument
    return render_template("result.html", info=info)