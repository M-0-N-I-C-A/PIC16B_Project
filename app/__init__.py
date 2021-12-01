from flask import Flask, g, current_app, render_template, request

import sqlite3

from tensorflow.keras import models

app = Flask(__name__)

@app.route("/")
def base():
    # render the base.html template
    return render_template("base.html")

"""
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
    height = request.form["height"]
    weight = request.form["weight"]
    systolic = request.form["systolic"]
    diastolic = request.form["diastolic"]

    # connect to the database
    db = get_info_db()

    # use a cursor to insert the message into the database
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO info (name, age, height, weight, systolic, diastolic) VALUES (?, ?, ?, ?, ?, ?)',
        (name, age, height, weight, systolic, diastolic)
    )
    # save the insertion
    db.commit()

    # close the database connection
    db.close()

    return(name, age, height, weight, systolic, diastolic)
"""

"""
@app.route("/submit/", methods = ["POST", "GET"])
def submit():
    # render the submit.html template in the GET case
    if request.method == "GET":
        return render_template("submit.html")
    # call the insert_info() function 
    # and render the submit.html with parameters
    # in the POST case
    else:
        name, age, height, weight, systolic, diastolic = insert_info(request)
        return render_template("submit.html", 
                               name=name,
                               age=age,  
                               height=height,
                               weight=weight, 
                               systolic=systolic, 
                               diastolic=diastolic)
"""

@app.route("/submit/", methods = ["POST", "GET"])
def submit():
    # render the submit.html template in the GET case
    if request.method == "GET":
        return render_template("submit.html")
    # call the insert_info() function 
    # and render the submit.html with parameters
    # in the POST case
    else:
        age = request.form["age"]
        gender = request.form["gender"]
        height = request.form["height"]
        weight = request.form["weight"]
        systolic = request.form["systolic"]
        diastolic = request.form["diastolic"]
        chol = request.form["chol"]
        gluc = request.form["gluc"]
        smoke = request.form["smoke"]
        alcohol = request.form["alcohol"]
        active = request.form["active"]

        model = models.load_model("cardio-model/model")
        r = model.predict(age, gender, height, weight, systolic, diastolic, chol, gluc, smoke, alcohol, active).argmax(axis = 1)

        return render_template('submit.html', risk=r)




"""
@app.route("/result/")
def result():
    db = get_info_db()



    model = pickle.load(open("../cardio-model/model.pkl", "rb"))
    model.predict()

    fig = px.histogram(df,
                       x = "weight",
                       width = 600,
                       height = 300)

    graphJSON = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
    # render the result.html template
    return render_template("result.html", graphJSON=graphJSON)
"""