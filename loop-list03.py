#Crie uma lista de 1 a 1 milhão,em seguida, use min() e max() a fim de garantir que sua lista realmente comece em 1 e termine em 1 milhao. 
#Alem disso,use a função sum() para ver a rapidez que o python pode efetuar a soma de um milhão de numeros.

lista = []
for num in range(1,1000001):
    lista.append(num)

print(f"O maior numero da lista é: {max(lista)}\nO menor numero da lista é: {min(lista)}\nA soma da lista inteira é: {sum(lista)}")

