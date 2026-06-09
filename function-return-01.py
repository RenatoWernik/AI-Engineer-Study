def calcular_area(altura,largura):
    return altura * largura 
    
area_sala = calcular_area(5,3)
print(f"A área da sala é: {area_sala}")
area_quarto = calcular_area(10,2)
print(f"A área do quarto é: {area_quarto}")
area_total = area_sala + area_quarto
print(f"A área total é: {area_total}")

