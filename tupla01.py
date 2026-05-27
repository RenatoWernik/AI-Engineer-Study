#Um restaurante com serviço de buffet oferece SOMENTE cinco refeiçoes. 
#Pense em cinco refeiçoes e armazeneas em uma tupla

refeicoes = ("Frango e arroz","Feijoada","Macarronada","Lasanha","Peixe grelhado")

# Use um loop for para exibir cada refeiçao que o restaurante oferece

print("As refeições disponíveis são: ")
for refeicao in refeicoes:
    print(f"\n{refeicao}")

#O restaurante mudoou o cardapio,substituindo duas refeições por outras diferentes.
#Adicione uma linha que reescreva a tupla e depois use um loop para exibir cada um dos elementos do menu atualizado.

refeicoes = ["Carne e Arroz","Escondidinho","Macarronada","Lasanha","Peixe Grelhado"]

print("\nO novo menu é: ")
for refeicao in refeicoes: 
    print(f"\n{refeicao}")

