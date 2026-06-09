def say_hi(names):
    for name in names:
        msg = f"Hi, {name.title()}!"
        print(msg)

usernames = ["Renato","Eduarda","Eduardo"]
say_hi(usernames)

#E se quisesse usar por algum motivo "return" nessa função?
