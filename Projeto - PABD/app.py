from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="labinfo",
        database="ajudaibd"
        )
    return conn

@app.route("/")
def index():
    return render_template("login.html") 

@app.route("/cadastro", methods=["POST"])
def cadastro():
    nome = request.form["nome"]
    telefone = request.form["telefone"]
    nascimento = request.form["nascimento"]
    email = request.form["email"]
    senha = request.form["senha"]

    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO usuario (nome, telefone, nascimento, email, senha) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (nome, telefone, nascimento, email, senha))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect(url_for("sucesso"))

@app.route("/sucesso")
def sucesso():
    return "Usuário cadastrado com sucesso!"