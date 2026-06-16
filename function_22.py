def registrar_evento(nome_evento,**detalhes):
    detalhes["Nome do Evento"] = nome_evento
    eventos.append(detalhes)
    return detalhes


eventos = []

registrar_evento("Major CS2",país = "Alemanha",categoria = "Jogos eletronicos")
registrar_evento("Copa do mundo",país = "EUA",categoria = "Esportes")



def exibir_eventos(lista_eventos):
    for evento in lista_eventos:
        print(f"\n--- {evento.get("Nome do Evento")} ---")
        for chave,valor in evento.items():
            if chave != "Nome do Evento":
                print(f"    {chave.capitalize()}: {valor}")
        
        

exibir_eventos(eventos)

