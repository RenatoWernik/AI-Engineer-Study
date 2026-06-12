def gerar_perfil(primeiro_nome,ultimo_nome,**informacoes):
    informacoes["Primeiro Nome"] = primeiro_nome
    informacoes["Ultimo Nome"] = ultimo_nome
    return informacoes


renato = gerar_perfil("renato","wernik",idade = 23,cidade ="Lisboa")
print(renato)
