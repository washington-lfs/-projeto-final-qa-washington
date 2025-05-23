#teste de regressão
# Função que queremos testar (versão atual)
def formatar_texto(texto):
    """
    Versão 1.1 - Remove espaços extras e coloca em maiúsculas
    """
    if not isinstance(texto, str):
        raise ValueError("Entrada deve ser string")
    return ' '.join(texto.split()).upper()

# Teste de regressão (compara com resultados esperados salvos)
def test_regressao_formatador():
    # Casos de teste históricos (resultados conhecidos da versão estável)
    casos_teste = {
        "  olá   mundo  ": "OLÁ MUNDO",    # Espaços extras
        "sem-espaços": "SEM-ESPAÇOS",      # Texto sem espaços
        "123 abc": "123 ABC",               # Números e letras
        "": ""                             # String vazia
    }
    
    falhas = 0
    for entrada, saida_esperada in casos_teste.items():
        resultado = formatar_texto(entrada)
        if resultado != saida_esperada:
            print(f"❌ Regressão detectada! Entrada: '{entrada}'")
            print(f"    Esperado: '{saida_esperada}' | Obtido: '{resultado}'")
            falhas += 1
    
    if falhas == 0:
        print("✅ Todos os casos de teste passaram (sem regressões)")
    else:
        print(f"⚠️ Total de regressões: {falhas}/{len(casos_teste)}")

# Execução
test_regressao_formatador()
