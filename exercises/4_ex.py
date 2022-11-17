# 4.1
pizzas = ['pepperoni', 'margarita', 'di mara']
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza')

print('\nI really love pizza\n')

# 4.2
animals = ['dog', 'rabbit', 'cat']
for animal in animals:
    print(f'{animal.title()} is a great pet')
print('Any of this animals would make a great pet')

# 4.3
for value in range(1, 21):
    print(value)

# 4.4
digits = []
for value in range(1, 1_000_001):
    digits.append(value)
print(max(digits))

digits = [value for value in range(1, 1_000_001)]
# for digit in digits:
#    print(digit)
print(min(digits))

# 4.5
digits = [value for value in range(1, 1_000_001)]
print(min(digits))
print(max(digits))
print(sum(digits))

# 4.6
uneven_numbers = [value for value in range(1, 20, 2)]
print(uneven_numbers)

# 4.7
triples = [value for value in range(3, 30, 3)]
print(triples)

# 4.8
cubes = [value**3 for value in range(1, 10)]
for cube in cubes:
    print(cube)

# 4.9
cubes = []
for cube in range(1, 10):
    cubes.append(cube**3)
print(cubes)

cubes = []
for value in range(1, 10):
    cube = value**3
    cubes.append(cube)
print(cubes)

# 4.10
players = ['charly', 'zoya', 'vera', 'markus', 'ben', 'maria', 'luk']
print(f'The first three items in the list are: {players[:3]}')
print(f'The first three items in the middle list are: {players[3:6]}')
print(f'The last three items in the list are: {players[-3:]}')

# 4.11
pizzas = ['pepperoni', 'margarita', 'di mara']
friend_pizza = pizzas[:]
pizzas.append('salami')
friend_pizza.append('mushrooms')
print('My favourite pizza are:')
for pizza in pizzas:
    print(pizza)
print('\nMy friend\'s favourite pizza are:')
for pizza in friend_pizza:
    print(pizza)

# 4.12
pizzas = ['pepperoni', 'margarita', 'di mara']
friend_pizza = pizzas[:]
for pizza in pizzas:
    print(pizza)

# 4.13
dishes = ('pepperoni', 'margarita', 'salad', 'ice cream', 'pasta')
for dish in dishes:
    print(dish)
print('\nUpdates:')
dishes = ('pepperoni', 'margarita', 'salad', 'soup', 'potato')
for dish in dishes[-2:]:
    print(dish)
