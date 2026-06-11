"""def verificar_aprovacao(nome_aluno,nota_aluno):
    #se a nota for maior ou igual a 10 -> aluno aprovado
    #se a nota for menor que 10 -> aluno reprovado
    resultado_aluno = {"Nome do aluno":nome_aluno,"Nota do aluno":nota_aluno}
    if resultado_aluno["Nota do aluno"] < 10:
        print(f"\nAluno {resultado_aluno["Nome do aluno"].title()} foi reprovado(a) com nota {resultado_aluno["Nota do aluno"]}")
    else:
        print(f"\nAluno {resultado_aluno["Nome do aluno"].title()} foi aprovado(a) com nota {resultado_aluno["Nota do aluno"]}")

    return resultado_aluno

renato = verificar_aprovacao("renato",15)
print(renato)
eduarda = verificar_aprovacao("eduarda",9)
print(eduarda)
eduardo = verificar_aprovacao("eduardo",10)
print(eduardo)"""

#Rescrevendo com as melhorias:

def verificar_aprovacao(nome_do_aluno,nota_do_aluno):
    if nota_do_aluno < 10:
        texto = f"{nome_do_aluno.title()} foi reprovado com nota {nota_do_aluno}"
        return texto
    elif nota_do_aluno == 20:
        texto = f"{nome_do_aluno.title()} foi aprovado com nota máxima! Parabéns!"
        return texto
    else:
        texto = f"{nome_do_aluno.title()} foi aprovado com nota {nota_do_aluno}"
        return texto
    

renato = verificar_aprovacao("renato",20)
print(renato)
eduarda = verificar_aprovacao("eduarda",15)
print(eduarda)
steve = verificar_aprovacao("steve",8)
print(steve)

