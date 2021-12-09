from flask import Flask, g, current_app, render_template, request

import pickle

# create a Flask object
app = Flask(__name__)

# root directory of our webapp
@app.route("/")
def base():
    # render the base.html template
    return render_template("base.html")

# ensure the submission page supports both POST and GET methods
@app.route("/submit/", methods = ["POST", "GET"])
def submit():
    # render the submit.html template in the GET case
    if request.method == "GET":
        return render_template("submit.html")
    # render the submit.html with parameters in the POST case
    else:
        # extract information from request
        name = request.form["name"]
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

        # convert the information except the name as integers
        # and create a data frame that contains the information
        x = [[int(age), int(gender), int(height), float(weight), int(systolic), int(diastolic), int(chol), int(gluc), int(smoke), int(alcohol), int(active)]]

        # use pickle.load() to use the logistic regression model
        model = pickle.load(open("cardio-model/model.pkl", 'rb'))
        # predict the risk based on the information
        r = model.predict(x) + 1

        return render_template('submit.html', risk=r, name=name)