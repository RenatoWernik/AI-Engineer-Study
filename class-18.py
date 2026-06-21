class BuscarDocumentos:
    def __init__(self,base_dados):
        self.base_dados = base_dados

    def buscar(self,query):
        print(f"Buscando os documentos sobre '{query}' em {self.base_dados}")
        

    

class GeradorResposta:
    def __init__(self,modelo):
        self.modelo = modelo
    

    def gerar(self,query):
        print(f"Gerando a resposta para '{query}' com o modelo {self.modelo}")


class SistemaRAG:
    def __init__(self,base_dados,modelo):
        self.base_dados = base_dados
        self.modelo = modelo
        self.documento = BuscarDocumentos(self.base_dados)
        self.resposta = GeradorResposta(self.modelo)
    
    def responder(self,query):
        self.documento.buscar(query)
        self.resposta.gerar(query)
        
        
sys = SistemaRAG("base_juridica","opus 4.8")
sys.responder("Qual oitava clausula do contrato do cliente Renato Wernik?")


#Adicionar return ao buscador para passar ao gerador.
#-> encadeamento.