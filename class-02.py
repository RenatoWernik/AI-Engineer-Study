class Restaurant:
    def __init__(self,restaurant_name,cusine_type):
        self.number_served = 0
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type


    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name.title()}")
        print(f"We are a {self.cusine_type.title()} cusine")
    

    def open_restaurant(self):
        print(f"We are open right now,come visit us!\n")
    
    def read_number_served(self):
        print(f"Number of clientes served today in {self.restaurant_name.title()}: {self.number_served}")
    
    def update_number_served(self,served):
        self.number_served = served

    def increment_number_served(self,incrementation):
        self.number_served += incrementation


camaroes = Restaurant("camarões","brazilian")
camaroes.describe_restaurant()
camaroes.open_restaurant()


tempero_do_chefe = Restaurant("tempero do chefe","portuguesa")
tempero_do_chefe.describe_restaurant(),tempero_do_chefe.open_restaurant()

cozinha_cultural = Restaurant("cozinha cultural","nordestina")
cozinha_cultural.describe_restaurant()
cozinha_cultural.open_restaurant()
cozinha_cultural.read_number_served()
cozinha_cultural.number_served = 5
cozinha_cultural.read_number_served()
cozinha_cultural.update_number_served(29)
cozinha_cultural.read_number_served()
cozinha_cultural.increment_number_served(6)
cozinha_cultural.read_number_served()


