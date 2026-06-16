class Car:
    def __init__(self,make,model,year):
        self.model = model
        self.make = make
        self.year = year

    def describe_car(self):
        full_name = f"{self.make} {self.model} {self.year}"
        print(f"Here is the car information: {full_name}")
        return full_name
    
    def fill_gas_tank(self):
        print(f"Filled the gas tank of {self.model.title()}")



class EletricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = "70kw"
    
    def read_batery_size(self):
        print(f"{self.make.title()} {self.model.title()} battery size is: {self.battery}")
    
    def fill_gas_tank(self):
        print(f"The car {self.make.title()} {self.model.title()} doesen't have a gas tank.")
    



my_nissan_gtr = Car("nissan","gtr","2025")
my_nissan_gtr.describe_car()
my_nissan_gtr.fill_gas_tank()

my_tesla = EletricCar("tesla","model 3","2026")
my_tesla.describe_car()
my_tesla.read_batery_size()
my_tesla.fill_gas_tank()

