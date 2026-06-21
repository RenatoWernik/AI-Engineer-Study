class Animal:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def dormir(self):
        print(f"{self.nome.title()} está a dormir!")
    

class Cao(Animal):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)
    
    def latir(self):
        print(f"{self.nome.title()} está a latir!")



bred = Cao("bred",15)
bred.dormir()
bred.latir()