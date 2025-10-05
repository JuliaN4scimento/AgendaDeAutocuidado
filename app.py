from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(_name_)

def connectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # coloque seu usuário do MySQL
        password="senha123",  # coloque sua senha
        database="Ajudai"     # banco de dados
    )



# Página inicial
@app.route("/")
def index():
    return render_template("index.html")

# Cadastro
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        data_nasc = request.form.get("data_nasc")  # precisa bater com o name do HTML
        email = request.form.get("email")
        senha = request.form.get("senha")

        conn = connectar_banco()
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (nome, telefone, nascimento, email, senha) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (nome, telefone, data_nasc, email, senha))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for("login"))
    return render_template("cadastro.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        conn = connectar_banco()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha))
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()

        if usuario:
            return redirect(url_for("tipoagenda"))
        else:
            return "Login inválido!"
    return render_template("login.html")

# Escolha da agenda
@app.route("/tipoagenda")
def tipoagenda():
    return render_template("tipoagenda.html")


@app.route("/agenda_diaria", methods=["GET", "POST"])
def agenda_diaria():
    if request.method == "POST":
        dia = request.form.get("dia")
        tarefas = {hora: request.form.get(f"hora{hora}") for hora in ["05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22"]}
        return render_template("agenda_final.html", tipo="diária", dia=dia, tarefas=tarefas)
    return render_template("agenda_diaria.html")


@app.route("/agenda_semanal", methods=["GET", "POST"])
def agenda_semanal():
    if request.method == "POST":
        tarefas = {dia: request.form.get(dia) for dia in ["segunda","terca","quarta","quinta","sexta","sabado","domingo"]}
        return render_template("agenda_final.html", tipo="semanal", tarefas=tarefas)
    return render_template("agenda_semanal.html")


if _name_ == "_main_":
    app.run(debug=True)