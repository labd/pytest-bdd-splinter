from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/redirect/")
def redirect_page():
    return redirect("/subpage/")


@app.route("/subpage/")
def subpage():
    return render_template("subpage.html")


@app.route("/subpage/nested/")
def subpage_nested():
    return render_template("subpage_nested.html")


@app.route("/animations/")
def animations():
    return render_template("animations.html")


@app.route("/forms/")
def forms():
    return render_template("forms.html")
