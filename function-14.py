"""def calcular_media (lista_notas):
        soma = 0
        n_notas = len(lista_notas)
        while lista_notas:
            nota_atual = lista_notas.pop()
            soma += nota_atual
        media = soma / n_notas
        return media
        
        

notas = [1,5,5,5]
resultado = calcular_media(notas)
print(resultado)


#poderia fazer esse exercicio usando sum() e len()
#tambem poderia fazer esse exercicio sem usar o return media,trocando essa linha por "print(media)"
#e fora da funçao apenas chamar "calcular_media(notas)"""


#Rescrevendo o codigo usando sum() e len()

def calcular_media(lista_de_notas):
    media = sum(lista_de_notas) / len(lista_de_notas)
    return media


notas_alunos =  [10,20,15,16,18,9,9,8]
media_turma = calcular_media(notas_alunos)
print(f"A media da turma é {round(media_turma)}")
print(notas_alunos)


