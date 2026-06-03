vendas = {
    "teclado": 45,
    "rato": 80,
    "monitor":12,
    "auscultadores":67,
    "webcam":30,
}

#Parte 1. Descobre qual foi o produto MAIS vendido e imprime uma frase do tipo "O produto mais vendido foi: X". Usa o max com key

top_product = max(vendas,key=vendas.get)
print(f"O produto mais vendido foi: {top_product.title()} com {vendas[top_product]} vendas")

#Parte 2. Descobre qual foi o produto MENOS vendido e imprime "O produto menos vendido foi: X"

bottom_product= min(vendas,key=vendas.get)
print(f"O produto menos vendido foi {bottom_product.title()} com {vendas[bottom_product]} vendas")

#Parte 3, a mais desafiante. Imprime os produtos ordenados do mais vendido para o menos vendido, cada um na sua linha, no formato 
#"rato: 80 unidades".

print("\nOs items mais vendidos em ordem foram:\n")


for item in sorted(vendas,key=vendas.get,reverse=True):
    print(f"{item.title()}: {vendas[item]} vendas")