class Memoria:
    def __init__(self):
        self.historico = []

    def adicionar(self,texto):
        self.historico.append(texto)
        
    def mostrar_historico(self):
        for msg in self.historico:
            print(f"-{msg}")


class Configuracao:
    def __init__(self,temperatura):
        self.temperatura = temperatura
    
    
    def mostrar_config(self):
        print(f"Configuração atual: {self.temperatura}")
    

class AgenteIA:
    def __init__(self,nome,temperatura):
        self.nome = nome
        self.temperatura = temperatura
        self.mem = Memoria()
        self.config = Configuracao(self.temperatura)

    
    def conversar(self,texto):
        self.mem.adicionar(texto)
        print(f"{self.nome.title()} recebeu {texto}")



opus = AgenteIA("opus",0.7)
opus.conversar("Crie um relatorio da minha semana")
opus.conversar("Capital do Brasil?")
opus.mem.mostrar_historico()
