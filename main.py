from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

#Cria instância do Flask
app = Flask(__name__)

#Rota para exibe formulário
@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
       # Consta o nome do formulário
      nome = request.form['nome']
      datacad = request.form['datacad']
      email = request.form['email']
      telefone = request.form['telefone']
      conn = mysql.connector.connect(host="localhost", user="root", password="", database="mdcsite")
      cursor = conn.cursor()
      cursor.execute("""insert into clientes(nome_cliente, data_cadastro, email_cliente, telefone_cliente) values (%s,%s,%s,%s)""", (nome, datacad, email, telefone))
      conn.commit()
      return redirect(url_for('login', nome=nome, datacad=datacad, email=email, telefone=telefone))
   # Executa o código HTML junto com o formulário
   return render_template('index.html')

#Rota para exibir a saudação personalizada
@app.route('/login/<nome>/<datacad>/<email>/<telefone>')
def login(nome, datacad, email, telefone):
   return render_template('login.html', nome=nome, datacad=datacad, email=email, telefone=telefone)

@app.route('/adm-clientes')
def clientes():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="mdcsite")
    cursor = conn.cursor()
    sql = "SELECT * FROM clientes"
    cursor.execute(sql)
    lista_clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("adm-clientes.html", lista_clientes=lista_clientes)

@app.route('/adm-produtos')
def adm_produtos():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="mdcsite")
    cursor = conn.cursor()
    sql = "SELECT * FROM produtos"
    cursor.execute(sql)
    lista_produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("adm-produtos.html", lista_produtos=lista_produtos)

@app.route('/adm')
def adm():
   return render_template("adm.html")

@app.route('/agendamento')
def agendamento():
   return render_template("agendamento-inicio.html")

@app.route('/produtos')
def produtos():
   return render_template("produtos.html")

@app.route('/micropigmentacao')
def micropigmentacao():
   return render_template("micropigmentacao.html")

@app.route('/cliente/<id_cliente>')
def deletar(id_cliente):
   if request.method == 'POST':
      conn = mysql.connector.connect(host="localhost", user="root", password="", database="crm_flask")
      cursor = conn.cursor()
      cursor.execute("""delete from cliente where id_cliente = %d""", (id_cliente))
      conn.commit()
   return render_template('clientes.html')

if __name__ == '__main__':
   app.run(debug=True)
