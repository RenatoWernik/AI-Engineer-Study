#Slicing: 
#Em uma lista, use slicing para exibir uma mensagem dos três primeiros items 
#Depois:Três items do meio 
#Depois:Três ultimos items de uma lista.

meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
print(f"Os três primeiros meses do ano são: {", ".join(meses[:3])}")
print(f"Os três meses do meio do ano são: {", ".join(meses[3:6])}")
print(f"Os três ultimos meses do ano são: {", ".join(meses[-3:])}")
