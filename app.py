from flask import Flask, g, current_app, render_template, request

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("base.html")