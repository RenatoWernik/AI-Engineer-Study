class Dispositivo:
    def __init__(self,marca,preco):
        self.marca = marca
        self.preco = preco
    
    
    def ligar(self):
        print(f"{self.marca.title()} ligado!")
    


class Telemovel(Dispositivo):
    def __init__(self,marca,preco,so):
        self.so = so
        super().__init__(marca,preco)

    
    def fazer_chamada(self):
        print(f"{self.marca.title()} a ligar para 0802123")
    

class Smartphone(Telemovel):
    def __init__(self,marca,preco,so,armazenamento):
        self.armazenamento = armazenamento
        super().__init__(marca,preco,so)

    
    def ligar(self):
        print(f"{self.marca.title()} - {self.preco} - SO: {self.so.title()} - Armazenamento: {self.armazenamento}")




iphone_17 = Smartphone("apple",1600,"IOS","256 gb")
iphone_17.ligar()
iphone_17.fazer_chamada()