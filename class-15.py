class Escola:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade


    def apresentar(self):
        print(f"Meu nome é {self.nome.title()} e tenho {self.idade} anos de idade")


class Aluno(Escola):
    def __init__(self,nome,idade,ano):
        super().__init__(nome,idade)
        self.ano = ano

class Professor(Escola):
        def __init__(self,nome,idade,materia):
            super().__init__(nome,idade)
            self.materia = materia


class Assistente(Escola):
    def __init__(self,nome,idade,bloco):
        super().__init__(nome,idade)
        self.bloco = bloco
    



aluno_1 = Aluno("Renato",17,2)
aluno_1.apresentar()


    


