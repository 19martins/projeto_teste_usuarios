from flask import Flask, render_template, request, redirect, url_for, flash
from servico_usuario import ServicoUsuario, Usuario, EmailJaExisteException, CredenciaisInvalidasException


app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Instância do serviço de usuário
servico_usuario = ServicoUsuario()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)
            servico_usuario.cadastrar_usuario(usuario)
            flash('Usuário cadastrado com sucesso!', 'success')
            return redirect(url_for('index'))
        except EmailJaExisteException:
            flash('Erro: O email já está em uso.', 'danger')
        except ValueError as e:
            flash(f'Erro: {str(e)}', 'danger')

    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        try:
            servico_usuario.login(email=email, senha=senha)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('index'))
        except CredenciaisInvalidasException:
            flash('Erro: Credenciais inválidas.', 'danger')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
