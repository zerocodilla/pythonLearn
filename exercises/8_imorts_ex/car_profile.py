# 8.16
import car_info

car = car_info.car_info('ford', 'focus', color='white', release_date=2018)
print(car)

from car_info import car_info

car = car_info('nissan', 'x-trail', color='black', release_date=2017)
print(car)

from car_info import car_info as ci

car = ci('nissan', 'x-trail', color='black', release_date=2017)
print(car)

import car_info as ci

car = ci.car_info('nissan', 'juke', color='black', release_date=2022)
print(car)
