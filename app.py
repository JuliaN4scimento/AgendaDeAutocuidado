from flask import Flask 
from flask import render_template, request, redirect, url_for, session, flash
import mysql.connector as connection 

app = Flask(__name__)

app.secret_key = "segredo123"

@app.route ("/")
def conexao ():
    cnx = connection.MySQLConnection (
        host="127.0.0.1",
        user="root", 
        password="labinfo",
        database="ajudaibd"
    )

    cursor = cnx.cursor (dictionary = True)
    cursor.execute ("SELECT nome, telefone, data_nasc, email, senha FROM usuarios")
    
    resultado = cursor.fetchall ()

    return render_template ("cadastro.html", banco = resultado)
 
@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

