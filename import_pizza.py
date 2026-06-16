def criar_pizza(size,*toppings):
    print(f"Making a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping.title()}")



def criar_sanduiche(size,*toppings):
    print(f"Preparing a {size}-inch sandwich with the following toppings: ")
    for topping in toppings:
        print(f"-{topping.title()}")