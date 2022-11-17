import car, electric_car

my_ford = car.Car('ford', 'focus', 2018)
print(my_ford.get_descriptive_name())

my_tesla = electric_car.ElectricCar('tesla', 'S', 2022)
print(my_tesla.get_descriptive_name())