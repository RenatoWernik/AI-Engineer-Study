class Processador:
    def __init__(self,nucleos):
        self.nucleos = nucleos

    def processar(self):
        print(f"O processador tem {self.nucleos} nucleos")
        print(f"O processador de {self.nucleos} nucleos está trabalhando!\n")

    
class MemoriaRAM:
    def __init__(self,tamanho_gb):
        self.tamanho_gb = tamanho_gb
    
    def carregar(self):
        print(f"A memoria tem {self.tamanho_gb} Gb\n")
    


class Computador:
    def __init__(self,marca,nucleos,tamanho_gb):
        self.marca = marca
        self.cpu = Processador(nucleos)
        self.ram = MemoriaRAM(tamanho_gb)
    

    def arrancar(self):
        print(f"PC {self.marca} ligando")
        self.cpu.processar()
        self.ram.carregar()
    

    
     



macbook = Computador("apple",12,16)
macbook.arrancar()