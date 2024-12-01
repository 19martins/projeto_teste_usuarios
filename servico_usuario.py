
class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class EmailJaExisteException(Exception):
    pass

class CredenciaisInvalidasException(Exception):
    pass

class ServicoUsuario:
    def __init__(self):
        self.usuarios = []

    def limpar_todos_os_usuarios(self):
        self.usuarios.clear()

    def cadastrar_usuario(self, usuario):
        # Verifica se o email já está cadastrado
        for u in self.usuarios:
            if u.email == usuario.email:
                raise EmailJaExisteException("O email já está cadastrado.")
        
        # Valida a senha (exemplo simplificado)
        if len(usuario.senha) < 8 or not any(char.isdigit() for char in usuario.senha):
            raise ValueError("A senha deve ter pelo menos 8 caracteres e incluir um número.")
        
        self.usuarios.append(usuario)

    def login(self, email, senha):
        for usuario in self.usuarios:
            if usuario.email == email and usuario.senha == senha:
                return True
        raise CredenciaisInvalidasException("Credenciais inválidas.")
