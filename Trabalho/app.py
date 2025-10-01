from flask import Flask, render_template, request, redirect, url_for
from controller import StreamingController

app = Flask(__name__)
controller = StreamingController()

@app.route('/', methods=['GET','POST'])
def login():
    erro = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if controller.login(usuario, senha):
            return redirect(url_for('index'))
        else:
            erro = "Usuário ou senha incorretos"
    return render_template('login.html', erro=erro)

@app.route('/index')
def index():
    disponiveis = controller.listar_disponiveis()
    destaque = controller.listar_destaque()
    return render_template('index.html', disponiveis=disponiveis, destaque=destaque)

@app.route('/adicionar_midia', methods=['POST'])
def adicionar_midia():
    titulo = request.form['titulo']
    genero = request.form['genero']
    avaliacao = float(request.form['avaliacao'])
    ano = int(request.form['ano'])
    idioma = request.form['idioma']

    temporada = request.form.get('temporada')
    episodio = request.form.get('episodio')

    # Se estiver vazio ou inválido, colocar 0
    temporada = int(temporada) if temporada and temporada.isdigit() else 0
    episodio = int(episodio) if episodio and episodio.isdigit() else 0

    controller.adicionar_midia(titulo, genero, avaliacao, ano, idioma, temporada, episodio)
    return redirect(url_for('index'))

@app.route('/destacar/<int:indice>')
def destacar(indice):
    controller.destacar_midia(indice)
    return redirect(url_for('index'))

@app.route('/remover/<int:indice>')
def remover(indice):
    controller.remover_midia(indice)
    return redirect(url_for('index'))

@app.route('/remover_destaque/<int:indice>')
def remover_destaque(indice):
    controller.remover_destaque(indice)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
