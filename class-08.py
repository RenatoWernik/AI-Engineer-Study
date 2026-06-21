# Classe independente que representa um Motor. Ela cuida de suas próprias regras (como ligar e potência).
class Motor:
    def __init__(self,potencia):
        self.potencia = potencia
    
    def ligar(self):
        print(f"Motor de {self.potencia} cv ligado!")
    

# CONCEITO DE COMPOSIÇÃO ("Tem um"): 
# Uma Moto não é um Motor, portanto ela não herda de Motor.
# Em vez disso, a Moto possui (é composta por) um Motor.
class Moto:
    # O construtor da Moto recebe os dados da Moto e a potência desejada para o seu motor.
    def __init__(self,marca,modelo,potencia):
        self.marca = marca
        self.modelo = modelo
        # Criamos uma instância de Motor diretamente dentro do construtor da Moto.
        # Agora, o atributo self.motor armazena um objeto do tipo Motor.
        self.motor = Motor(potencia)

    def arrancar(self):
        print(f"Ligando motor")
        # Delegação: A Moto não sabe como um motor funciona internamente.
        # Por isso, ela delega a ação ao objeto motor que ela possui chamando .ligar()
        self.motor.ligar()
    

# Cria uma Moto com marca "honda", modelo "cbr" e potência de "223" cv.
# Internamente, a Moto cria um Motor de 223 cv.
cbr = Moto("honda","cbr",223)
cbr.arrancar()

