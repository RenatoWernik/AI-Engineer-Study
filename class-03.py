class User:
    def __init__(self,first_name,last_name,age,status):
        self.login_attempts = 0
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.status = status
    
    
    def describe_user(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}" 
        print(f"Here are the informations about the user {full_name}: ")
        print(f"User age: {self.age}")
        print(f"User status: {self.status.title()}")
    

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}\n")

    def increment_login(self):
        self.login_attempts += 1
        print(f"{self.first_name.title()} incremented the login attempt.\n Login attempts: {self.login_attempts} (The max loggin attempts is 3)")

    def reset_login(self):
        self.login_attempts = 0
        print(f"Reseted login attempts.\n Login attempts = {self.login_attempts}")

        
renato = User("renato","wernik",23,"active")
renato.describe_user()
renato.greet_user()
        
        
eduarda = User("eduarda","wernik",22,"paused")
eduarda.describe_user()
eduarda.greet_user()


steve = User("steve","jobs",23,"active")
steve.describe_user()
steve.greet_user()
steve.increment_login()
steve.increment_login()
steve.increment_login()
steve.reset_login()
steve.increment_login()
