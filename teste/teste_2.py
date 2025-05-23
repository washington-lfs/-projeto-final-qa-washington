#teste de integração

# Sistema de usuários simplificado
usuarios = {}

def cadastrar_usuario(nome, senha):
    if nome in usuarios:
        return False  # Usuário já existe
    usuarios[nome] = senha
    return True

def fazer_login(nome, senha):
    return usuarios.get(nome) == senha

# Teste de integração
def test_fluxo_login():
    # 1. Cadastra um novo usuário
    cadastro_ok = cadastrar_usuario("alice", "senha123")
    assert cadastro_ok is True, "Cadastro falhou"
    
    # 2. Testa login com credenciais corretas
    login_ok = fazer_login("alice", "senha123")
    assert login_ok is True, "Login válido falhou"
    
    # 3. Testa login com senha errada
    login_invalido = fazer_login("alice", "errada")
    assert login_invalido is False, "Login inválido passou"
    
    print("✅ Teste passou - Fluxo completo validado!")

# Executa
test_fluxo_login()
