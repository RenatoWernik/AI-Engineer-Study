def criar_perfil(primeiro_nome,ultimo_nome,idade=None,cidade=None,profissao=None):
    person = {"primeiro":primeiro_nome.title(),"ultimo":ultimo_nome.title()}
    if idade or cidade or profissao:
        person["idade"] = idade
        person["cidade"] = cidade.title()
        person["profissao"] = profissao.title()
        #quando aprender os **kwargs esse problema desaparece.
    return person

perfil = criar_perfil("renato","wernik",23,"lisboa","programador").items()
print("Esses foram os dados introduzidos pelo usuário: ")
for chave,value in perfil:
    print(f"\t{chave.title()} - {value}")



