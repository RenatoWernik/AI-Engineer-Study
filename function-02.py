def describe_pet(animal_type,pet_name):
    print(f"I have a {animal_type} and his name is {pet_name.title()}")

describe_pet(animal_type="dog",pet_name="bred")

#isso é um exemplo de argumentos nomeados.
#describe_pet(animal_type="dog",pet_name="bred") e describe_pet(pet_name="bred",animal_type="dog") geram o mesmo resultado

def fav_color(name,color="blue"):
    print(f"My name is {name.title()} and my favorite color is {color}")

fav_color("renato")

#Definimos o valor Default de "color" como blue
#Dessa forma,quando não passarmos um valor para color ao chamar a função,o valor vai ser passado automaticamente como blue

