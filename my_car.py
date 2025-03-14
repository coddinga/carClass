from car_class import Car
from electric_car_class import ElectricCar

my_car = Car('ford', 'explorer', 2014)
print(my_car.get_info())

my_car.update_odometer(23)
my_car.read_odometer()

my_car.increment_odometer(10)
my_car.read_odometer()

#electric car
my_ecar = ElectricCar('tesla', 'model s', 2019)
print(my_ecar.get_info())

my_ecar.battery.describe_battery()
my_ecar.battery.get_range()
