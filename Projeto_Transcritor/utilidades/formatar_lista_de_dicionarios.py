def formatar_lista(lista_para_formatar):
    lista_string = ""
    for num,dic in enumerate(lista_para_formatar):
        nome = dic["pessoa"]
        fala = dic["fala"]
        lista_string += f"[{num + 1}] {nome}: {fala}\n"
    return lista_string