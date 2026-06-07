name = input("What is your name? ")
age = int(input("How old are you? "))
def greet_user(name,age):
    print(f"Hello, {name.title()}")
    if age > 18 :
        print("You are allowed to drive!")
    else:
        print("You are not allowed to drive yet.")

greet_user(name,age)
#name - parâmetro
#"RENATO" - argumento
#isso foi um exemplo de função com argumentos posicionais.