from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)
@app.route("/")
def home():

    return render_template("login.html")


@app.route("/cadastro"), methods=("get")
def cadastro():

    if request.methods == "POST":


        id = request.form.get