age = int(input("How old are you? "))
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is: ${price}")


#topping = input("Digite seu topping")
#print(f"Seu topping é {topping}")


#topping = [input("Quais toppings você quer?")]
#print(topping)

