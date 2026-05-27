#Copiando listas com slicing.
#Crie uma primeira lista contendo items,depois,usando slicing,copie essa lista para uma segunda e nova lista.
#Depois, adicione items diferentes a cada lista e prove que cada uma é uma lista separada 
#exibindo uma mensagem que exiba cada item de cada lista usando um loop For.


minhas_pizzas = ["Quatro Queijos","Calabresa","Costela"]
pizzas_duda = minhas_pizzas[:]

minhas_pizzas.append("Frango")

for pizza in minhas_pizzas:
    print(pizza)
print("São minhas pizzas favoritas")

pizzas_duda.append("Portuguesa")

print(f"As pizzas favotitas da duda são: {[pizza for pizza in pizzas_duda]}")
