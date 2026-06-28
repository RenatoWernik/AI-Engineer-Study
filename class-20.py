class ModeloLLM:
    def __init__(self,nome):
        self.nome = nome
    
    def chamar(self,prompt):
        print(f"{self.nome.title()} respondendo: {prompt}")
    

class ModeloClaude(ModeloLLM):
    def __init__(self,nome):
        super().__init__(nome)
        
    
    def chamar(self,prompt):
        super().chamar(prompt)
        print(f"Provedor: {self.nome.title()}")
    

class ModeloGPT(ModeloLLM):
    def __init__(self,nome):
        super().__init__(nome)
    
    def chamar(self,prompt):
        super().chamar(prompt)
        print(f"Provedor: {self.nome.title()}")



class Configuracao:
    def __init__(self,temperatura):
        self.temperatura = temperatura
    

class Agente:
    def __init__(self,nome,temperatura,modelo):
        self.nome = nome
        self.temperatura = temperatura
        self.config = Configuracao(temperatura)
        self.modelo = modelo

    def executar(self,prompt):
        self.modelo.chamar(prompt)

    
class Orquestrador:
    def __init__(self):
        self.lista_agentes = []
    
    def adicionar_agentes(self,agente):
        self.lista_agentes.append(agente)
    
    def executar_todos(self,prompt):
        for a in self.lista_agentes:
            a.executar(prompt)
    


modelo_claude = ModeloClaude("Opus")
agente_claude = Agente("Opus_ChatBot",0.8,modelo_claude)
lang_chain = Orquestrador()
lang_chain.adicionar_agentes(agente_claude)
lang_chain.executar_todos("Qual a capital da Inglaterra?")

modelo_gpt = ModeloGPT("GPT Mini")
agente_gpt = Agente("ChatBot_GPT",0.9,modelo_gpt)
lang_chain.adicionar_agentes(agente_gpt)
lang_chain.executar_todos("Como saber se estou preparado para começar Langchain e LangGraph?")




