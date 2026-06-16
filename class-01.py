class Aluno:
    def __init__(self,name,score):
        self.name = name
        self.score = score
        if score >= 7:
            print(f"Aluno {name.title()} aprovado com nota {score}")
        else:
            print(f"Aluno {name.title()} reprovado com nota {score}")
        
    def studying(self):
        print(f"O aluno {self.name.title()} esta estudando")


renato = Aluno("renato",10)
renato.studying()
