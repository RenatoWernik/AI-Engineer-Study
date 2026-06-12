def construir_pedido(modelo,mensagem,**kwargs):
    kwargs["Model"] = modelo
    kwargs["Prompt"] = mensagem
    return kwargs


chamada = construir_pedido("Opus 4.8","Build me a landing page",temperature = 0.8,max_tokens = 500000)
print(chamada)
