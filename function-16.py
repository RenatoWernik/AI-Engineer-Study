"""def criar_aluno(nome_aluno,nota_aluno):
    info_aluno = {"Nome do aluno": nome_aluno, "Nota aluno": nota_aluno}
    if info_aluno["Nota aluno"] < 10:
        info_aluno["Situação"] = "Reprovado"
    else:
        info_aluno["Situação"] = "Aprovado"
    return info_aluno

aluno_renato = criar_aluno("renato",15)
aluno_eduardo = criar_aluno("eduardo",9)
aluno_eduarda = criar_aluno("eduarda",10)
aluno_steve = criar_aluno("steve",15)
lista_alunos = [aluno_renato,aluno_eduardo,aluno_eduarda,aluno_steve]


def mostrar_relatorio(alunos):
    for aluno_info in alunos:
        print(aluno_info)

mostrar_relatorio(lista_alunos)
#Como posso deixar esse output mais limpo? para não sair "{'Nome do aluno': 'steve', 'Nota aluno': 15, 'Situação': 'Aprovado'}"""

#Rescrevendo o código com melhorias

# -> Lista vazia e ir fazendo .append()
# dicionario["chave"].title()


def criar_aluno(nome_do_aluno,nota_do_aluno):
    dicionario = {"nome": nome_do_aluno,"nota":nota_do_aluno}
    if nota_do_aluno < 10:
        dicionario["situacao"] = "reprovado"
        return dicionario
    else:
        dicionario["situacao"] = "aprovado"
        return dicionario

def mostrar_relatorio(lista_de_dicionarios_de_alunos):
    for aluno in lista_de_dicionarios_de_alunos:
        print(f"Nome - {aluno["nome"].title()}")
        print(f"Nota - {aluno["nota"]}")
        print(f"Situação - {aluno["situacao"].title()}\n")
        
        



lista_de_alunos = []
lista_de_alunos.append(criar_aluno("renato",20))
lista_de_alunos.append(criar_aluno("eduarda",16))
lista_de_alunos.append(criar_aluno("steve",8))


mostrar_relatorio(lista_de_alunos)


