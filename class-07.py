class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

    def descrever(self):
        print(f"{self.nome.title()} recebe {self.salario} euros")


class Gerente(Funcionario):
    # Construtor da classe Gerente. Para criar um gerente, precisamos de 3 informações:
    # o nome, o salário e o tamanho da equipe.
    def __init__(self,nome,salario,equipa):
        # super() refere-se à classe pai (Funcionario). Chamamos o __init__ dela
        # para inicializar nome e salario, evitando reescrever código (Princípio DRY).
        super().__init__(nome,salario)
        # Como a classe pai (Funcionario) não sabe e nem precisa saber sobre equipes,
        # salvamos essa informação específica apenas aqui na classe Gerente.
        self.equipa = equipa
    
    def descrever(self):
        print(f"{self.nome.title()} recebe {self.salario} euros\nTamanho da equipe de {self.nome.title()}: {self.equipa} pessoas")
    


renato = Funcionario("renato",1700)
renato.descrever()

kayo = Gerente("kayo",2500,9)
kayo.descrever()