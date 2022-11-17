from car import Car
from electric_car import ElectricCar as EC

car_1 = Car('nissan', 'x-trail', 2017)
print(car_1.get_descriptive_name())

car_2 = EC('nissan', 'leaf', 2021)
print(car_2.get_descriptive_name())