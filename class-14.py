class Animal:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def comer(self):
        print(f"{self.nome.title()} está comendo!")

    def dormir(self):
        print(f"{self.nome.title()} está dormindo....")
    
    def info(self):
        print(f"{self.nome.title()} tem {self.idade} anos")

    

class Gato(Animal):
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        super().__init__(nome,idade)
    
    def miar(self):
        print(f"-{self.nome.title()}: Miau!")
    
class Cachorro(Animal):
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        super().__init__(nome,idade)
    
    def latir(self):
        print(f"-{self.nome.title()}: Au Au!")


kitty = Gato("Kitty",5)
kitty.comer()
kitty.dormir()
kitty.info()
kitty.miar()
print("\n")
spike = Cachorro("spike",8)
spike.comer()
spike.dormir()
spike.info()
spike.latir()


