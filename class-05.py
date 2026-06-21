class Car:
    def __init__(self,make,model,year,millage):
        self.make = make
        self.model = model
        self.year = year
        self.millage = millage     
    

    def read_car(self):
        formated_name = f"{self.make.title()} {self.model.title()} {self.year}"
        print(f"\n--- Car Information ---\n")
        print(f"\t{formated_name} with {self.millage} kms on it")

    def fill_gas_tank(self):
        print(f"Filled the car tank!")

    
    def increment_milage(self,add_to_millage):
        self.millage += add_to_millage
        print(f"Now the car has {self.millage} kms on it")


    
    


class Battery:
    def __init__(self,battery_size = 40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size} kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} kms on full charge.")



class EletricCar(Car):
    def __init__(self,make,model,year,millage):
        super().__init__(make,model,year,millage)
        self.battery = Battery()

        
    def fill_gas_tank(self):
        print(f"{self.make.title()} {self.model.title()} is a eletric car, you cant fill the tank!")


first_car = Car("nissan","gtr","2026",20_000)
first_car.read_car()
first_car.increment_milage(2_000)


tesla_model_3 = EletricCar("tesla","model 3",2026,900)
tesla_model_3.read_car()
tesla_model_3.increment_milage(100)
tesla_model_3.battery.describe_battery()
tesla_model_3.battery.get_range()
tesla_model_3.fill_gas_tank()






