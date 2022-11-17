from electric_car import ElectricCar

el_car = ElectricCar('nissan', 'leaf', '2014')
print(el_car.get_descriptive_name())
el_car.battery.describe_battery()
el_car.battery.get_range()
el_car.battery.upgrade_battery()
el_car.battery.describe_battery()
el_car.battery.get_range()


