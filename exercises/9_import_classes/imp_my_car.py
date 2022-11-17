from car import Car

my_car = Car('ford', 'focus', 2018)
print(my_car.get_descriptive_name())
my_car.read_odometer()

# Modify Attribute Values
# directly:
my_car.odometer = 23
my_car.read_odometer()

# change value through method
my_car.update_odometer(33)
my_car.read_odometer()

# Incrementing an attribute’s Value through a Method
car_1 = Car('subaru', 'outback', 2013)
print(car_1.get_descriptive_name())
car_1.update_odometer(23500)
car_1.read_odometer()
car_1.increment_odometer(100)
car_1.read_odometer()
car_1.increment_odometer(-100)
car_1.read_odometer()



