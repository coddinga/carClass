class Car:
    """Description of a car"""
    def __init__(self, make, model, year):
        self.make = model
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_info(self):
        car_info = f"{self.year} {self.make} {self.model}"
        return car_info.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it. ")
    
    def update_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("Roll back not allowed. ")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
    def fill_gas(self):
        print("Gas tank is full!")
