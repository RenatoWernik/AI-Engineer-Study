sandwich_orders = ["pastrami","bigmc","cheeseburger","bacon","vegan"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)

print(",".join(finished_sandwiches))
print(sandwich_orders)