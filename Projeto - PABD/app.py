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


'''from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', 
                                 password='labinfo',
                                 host='127.0.0.1',
                                 database='ajudai'
                                 )
cursor = cnx.cursor() # inicio do bd

sql = "insert into pessoa(nome, telefone, nascimento, email, senha) \
values (%s,%s,%s,%s,%s)"

nome = 'giovanna'
telefone = '84994611428'
nasc = '2007-04-09'
email ='o.giovanna@escolar.ifrn.edu.br'
senha = '2222'

dados = (nome,telefone,nasc,email,senha)


cursor.execute(sql, dados)
cnx.commit()

cnx.close()'''