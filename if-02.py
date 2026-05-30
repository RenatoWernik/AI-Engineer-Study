requested_toppings = [input("What toppings you want to add to your pizza?")]
for topping in requested_toppings:
    print(f"Adding {topping}\n in your pizza")

print(f"Your pizza is ready with the requested toppings: \n{",".join(requested_toppings)}")