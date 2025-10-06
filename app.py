from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

#Aplicação flask
app = Flask(__name__)

#Conexão do banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="infoj",
    database="setembroAmarelo"
)

#Cria o cursor que executa os comandos do mysql
cursor = conexao.cursor()

#Rota da página inicial
@app.route('/')
def index():
    return render_template('index.html')

#Rota que salva os dados do formulário
@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    telefone = request.form['telefone']
    data_nasc = request.form['data_nasc']
    email = request.form['email']
    senha = request.form['senha']

    #Inserir os dados no banco
    comando = "INSERT INTO usuario (nome, telefone, nascimento, email, senha) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, telefone, data_nasc, email, senha)
    cursor.execute(comando, valores)
    conexao.commit()

    #Redireciona para o usuario escolher agenda
    return redirect(url_for('tipoagenda'))

#Rota da página de cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

#Rota da página para escolher agenda
@app.route('/tipoagenda')
def tipoagenda():
    return render_template('tipoagenda.html')

#Rotas de escolha de tipo de agenda
@app.route('/agendadiaria')
def agendadiaria():
    return render_template('agenda_diaria.html')

#Rotas da página da agenda semanal
@app.route('/agendasemanal')
def agendasemanal():
    return render_template('agenda_semanal.html')

#Rodar o flask
if __name__ == '__main__':
    app.run(debug=True)