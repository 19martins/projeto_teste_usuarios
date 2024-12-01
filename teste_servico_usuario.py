import pytest
from servico_usuario import ServicoUsuario, Usuario, EmailJaExisteException, CredenciaisInvalidasException

@pytest.fixture
def servico_usuario():
    return ServicoUsuario()

@pytest.fixture(autouse=True)
def limpar_usuarios(servico_usuario):
    servico_usuario.limpar_todos_os_usuarios()

# Testes para Cadastro de Usuário

def teste_cadastro_usuario_valido(servico_usuario):
    usuario = Usuario(nome="João Silva", email="joao.silva@exemplo.com", senha="Senha123")
    try:
        servico_usuario.cadastrar_usuario(usuario)
    except Exception:
        pytest.fail("Cadastro de usuário válido lançou uma exceção.")

def teste_cadastro_email_duplicado(servico_usuario):
    usuario1 = Usuario(nome="João Silva", email="joao.silva@exemplo.com", senha="Senha123")
    usuario2 = Usuario(nome="Maria Silva", email="joao.silva@exemplo.com", senha="Senha456")

    servico_usuario.cadastrar_usuario(usuario1)

    with pytest.raises(EmailJaExisteException):
        servico_usuario.cadastrar_usuario(usuario2)

def teste_cadastro_senha_invalida(servico_usuario):
    usuario = Usuario(nome="João Silva", email="joao.silva@exemplo.com", senha="123")  # Senha inválida
    with pytest.raises(ValueError):
        servico_usuario.cadastrar_usuario(usuario)

# Testes para Login

def teste_login_credenciais_validas(servico_usuario):
    usuario = Usuario(nome="João Silva", email="joao.silva@exemplo.com", senha="Senha123")
    servico_usuario.cadastrar_usuario(usuario)

    try:
        servico_usuario.login(email="joao.silva@exemplo.com", senha="Senha123")
    except Exception:
        pytest.fail("Login com credenciais válidas lançou uma exceção.")

def teste_login_senha_incorreta(servico_usuario):
    usuario = Usuario(nome="João Silva", email="joao.silva@exemplo.com", senha="Senha123")
    servico_usuario.cadastrar_usuario(usuario)

    with pytest.raises(CredenciaisInvalidasException):
        servico_usuario.login(email="joao.silva@exemplo.com", senha="SenhaErrada")

def teste_login_email_nao_cadastrado(servico_usuario):
    with pytest.raises(CredenciaisInvalidasException):
        servico_usuario.login(email="nao.existe@exemplo.com", senha="Senha123")
