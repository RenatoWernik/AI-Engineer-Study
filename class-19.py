class Ferramenta:
    def __init__(self,nome):
        self.nome = nome

    def executar(self,entrada):
        print(f"Executando ferramenta: {self.nome.title()} com: '{entrada}'")


class FerramentaBusca(Ferramenta):
    def __init__(self,nome):
        super().__init__(nome)
    
    def executar(self,entrada):
        super().executar(entrada)
        print("Buscando na web...\n")



class FerramentaCalculadora(Ferramenta):
    def __init__(self,nome):
        super().__init__(nome)
    
    def executar(self,entrada):
        super().executar(entrada)
        print("Calculando resultado...\n")
    

class AgenteIA:
    def __init__(self,nome):
        self.nome = nome
        self.ferramenta_busca = FerramentaBusca(nome)
        self.ferramenta_calculadora = FerramentaCalculadora(nome)

    def usar_ferramenta(self,nome_ferramenta,entrada):
        if nome_ferramenta == "busca":
            self.ferramenta_busca.executar(entrada)
        elif nome_ferramenta == "calculadora":
            self.ferramenta_calculadora.executar(entrada)
        else:
            print("Selecione 'busca' ou 'calculadora'")


chatbot = AgenteIA("Chat Bot Juridico")
chatbot.usar_ferramenta("calculadora","converta 5 euros em dolares")
chatbot.usar_ferramenta("busca","pesquise sobre as leis de LGPD")