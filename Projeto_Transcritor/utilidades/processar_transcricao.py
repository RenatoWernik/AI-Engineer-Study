def processar_transcricao(caminho_transcricao):
    with open(caminho_transcricao,encoding = "utf-8") as f:
        conteudo = f.read()

    blocos = conteudo.split("\n\n")

    lista_falas = []
    for bloco in blocos:
        if "<v" not in bloco:
            continue
        linhas_do_bloco = bloco.split("\n")
        linha_suja = " ".join(linhas_do_bloco[2:])
        linha_limpa = linha_suja.removeprefix("<v ").removesuffix("</v>")
        pessoa,fala = linha_limpa.split(">",1)
        lista_falas.append({"pessoa":pessoa,"fala":fala})
    
    return lista_falas