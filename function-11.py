def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("Please tell me your name: ")
    print("Enter 'quit' to exit at any time")
    f_name = input("First name: ")
    if f_name == "quit":
        break
    l_name = input("Last name: ")
    if l_name == "quit":
        break

    formatted_name = get_formatted_name(f_name,l_name)

    print(formatted_name)
