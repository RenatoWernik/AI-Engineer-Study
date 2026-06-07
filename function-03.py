def get_fullname(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
    
person = get_fullname("renato","wernik")    
print(person)