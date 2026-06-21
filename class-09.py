class ConfiguracaoModelo:
    def __init__(self,temperatura,max_tokens):
        self.temperatura = temperatura
        self.max_tokens = max_tokens

    def mostrar_config(self):
        print(f"Configurações:\nTemperatura: {self.temperatura}\nMax Tokens: {self.max_tokens}")


class ClienteLLM:
    def __init__(self,modelo,temperatura,max_tokens):
        self.modelo = modelo
        self.config = ConfiguracaoModelo(temperatura,max_tokens)

    
    def enviar_mensagem(self,msg):
        print(f"A enviar para o modelo({self.modelo}): {msg}")



cliente = ClienteLLM("Claude Opus 4.6",0.7,50_000)
cliente.enviar_mensagem("Gere um relatório do meu ultimo mês de estudos.")
cliente.config.mostrar_config()

