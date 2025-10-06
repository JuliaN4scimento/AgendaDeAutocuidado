from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="infoj",
    database="setembroAmarelo"
)
cursor = conexao.cursor()

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota que salva os dados do formulário
@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    telefone = request.form['telefone']
    data_nasc = request.form['data_nasc']
    email = request.form['email']
    senha = request.form['senha']

    comando = "INSERT INTO usuario (nome, telefone, nascimento, email, senha) VALUES (%s, %s, %s, %s, %s)"
    valores = (nome, telefone, data_nasc, email, senha)
    cursor.execute(comando, valores)
    conexao.commit()

    return redirect(url_for('tipoagenda'))  # volta para a tela inicial

# Página de cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

#pagina para escolher agenda
@app.route('/tipoagenda')
def tipoagenda():
    return render_template('tipoagenda.html')

#rotas de escolha de tipo de agenda
@app.route('/agendadiaria')
def agendadiaria():
    return render_template('agenda_diaria.html')

# Página da agenda semanal
@app.route('/agendasemanal')
def agendasemanal():
    return render_template('agenda_semanal.html')

if __name__ == '__main__':
    app.run(debug=True)