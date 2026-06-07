unconfirmed_users = ["brendon","dan","alan","paul","adrian"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
    print(f"Confirming the following user: {current_user.title()}")

print("\nConfirmed users: ")
print(",".join(confirmed_users).title())
