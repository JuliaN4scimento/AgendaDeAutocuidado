from flask import Flask, request, redirect, render_template
import mysql.connector

app = Flask(__name__)

cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='infoj',
    database='setembroAmarelo'
)

cursor = cnx.cursor()

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Rota para receber os dados do formulário e salvar no banco
@app.route('/salvar', methods=['POST'])
def salvar():
    # Pega os dados do formulário
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    data_nasc = request.form.get('nascimento')
    email = request.form.get('email')
    senha = request.form.get('senha')
    
    # Insere no banco de dados
    sql = "INSERT INTO usuarios (nome, telefone, nascimento, email, senha) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nome, telefone, data_nasc, email, senha))
    cnx.commit()
    
    # Redireciona ou mostra mensagem de sucesso
    return "Cadastro realizado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)