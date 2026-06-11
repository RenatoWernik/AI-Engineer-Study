def criar_perfil():
    informacao_usuario = {}

    informacao_usuario["primeiro"] = input("Digite seu primeiro nome: ")
    informacao_usuario["ultimo"] = input("Digite seu ultimo nome: ")
    while True:
        chave = input("Que tipo de informação você deseja acrescentar? (ou 'quit' para sair): ")
        if chave.lower() == "quit":
            break
        valor = input(f"Qual resposta para {chave} ? ")
        informacao_usuario[chave] = valor

    return informacao_usuario


#dicionario_perfil = criar_perfil()


def exibir_perfil(dicionario_perfil):
    print("\n ==== PERFIL ====")
    if "primeiro" in dicionario_perfil and "ultimo" in dicionario_perfil:
        print(f"Nome {dicionario_perfil["primeiro"].title()} {dicionario_perfil["ultimo"].title()}")
        
        for chave,valor in dicionario_perfil.items():
            if chave not in ("primeiro","ultimo"):
                print(f"{chave.title()}: {valor.title()}")

usuario = criar_perfil()
exibir_perfil(usuario)

