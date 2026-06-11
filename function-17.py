def criar_sanduiche(tamanho,*recheios):
    tamanho = int(input("Escolhe o tamanho do sanduiche (15 ou 30 cm) "))
    print(f"O tamanho do sanduiche é {tamanho}")
    print("Os recheios são:\n")
    for recheio in recheios:
        print(recheio.title())


criar_sanduiche("peperoni","queijo","alface")
criar_sanduiche("mustarda","carne","alface")