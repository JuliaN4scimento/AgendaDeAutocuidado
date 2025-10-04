from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def connectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario", 
        password="sua_senha",
        database="Ajudai"
    )

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        telefone = request.form["telefone"]

        conn = connectar_banco()
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (nome, email, senha, telefone) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, email, senha, telefone))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for("tipoagenda"))

    return render_template("index.html")

@app.route("/tipoagenda")
def tipoagenda():
    return render_template("tipoagenda.html")
