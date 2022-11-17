# import module
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'peper', 'cheese')

# import specific function
from pizza import make_pizza

make_pizza(16, 'cheese')


# function as alias
from pizza import make_pizza as mp

mp(7, 'cheese')

# alias for module
import pizza as p

p.make_pizza(2, 'cheese')


# import all functions of a module ! not recommended
from pizza import *

make_pizza(12, 'pepper')
