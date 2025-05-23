
# Módulo de banco de dados simulado
database = {}

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class ServicoUsuario:
    @staticmethod
    def criar_usuario(nome, email):
        if not email or '@' not in email:
            raise ValueError("Email inválido!")
        if email in database:
            raise ValueError("Email já cadastrado!")
        
        novo_usuario = Usuario(nome, email)
        database[email] = novo_usuario
        return novo_usuario

    @staticmethod
    def buscar_usuario(email):
        return database.get(email)

# Teste de Integração
def test_fluxo_completo_cadastro_usuario():
    # 1. Criação de usuário
    usuario = ServicoUsuario.criar_usuario("Ana Silva", "ana@exemplo.com")
    
    # 2. Verificação se o usuário foi persistido
    usuario_recuperado = ServicoUsuario.buscar_usuario("ana@exemplo.com")
    
    # 3. Asserts (verificações)
    assert usuario_recuperado is not None, "Usuário não foi salvo no banco de dados"
    assert usuario_recuperado.nome == "Ana Silva", "Nome do usuário incorreto"
    assert usuario_recuperado.email == "ana@exemplo.com", "Email do usuário incorreto"
    
    print("✅ Teste de integração passou com sucesso!")

# Executar o teste
if __name__ == '__main__':
    test_fluxo_completo_cadastro_usuario()
