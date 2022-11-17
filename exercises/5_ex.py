# 5.1
car = 'subaru'
if car == 'subaru':
    print('Is car == subaru? I predict True.')
    print(car)
if car != 'audi':
    print('\nIs car == audi? I predict False.')
    print(car)


age = 2
if age > 45:
    print('Please change passport')
else:
    print('Grow up!')

age = 2
if age > 1:
    print('true')

my_answer = 12
if my_answer != 0:
    print('Try again')

# this is the program, which tests all cars my family owned

parents_cars = ['lada', 'toyota']
my_cars = ['honda', 'ford']
john_cars = ['subaru', 'nissan']
my_first_car = 'honda'
my_current_car = 'Ford'
purchase_year = 2018
distance = 10000
since_last = 9  # months

if my_first_car == 'honda':
    print(f'1 {my_cars[0].title()} is my first car.')

if my_first_car != 'subaru':
    print(f'2 No, my first car was different.')

if my_current_car.lower() == 'ford':
    print(f'3 You are right. My first car is {my_current_car}.')

if purchase_year >= 2018:
    print(f'4 You owns the car less then 5 years')

if purchase_year <= 2012:
    print(f'5 Your car is old. Time to change')
else:
    print('5 Your car is new')

if purchase_year == 2018:
    print(f'6 You bought your car in {purchase_year}.')

if purchase_year >= 2019 and distance <= 15000:
    print('7 Your car is in guarantee period.')
else:
    print('7 Your guarantee has ended')

if since_last >= 12 or distance >= 10000:
    print('8 You need to change oil!')

if 'audi' in my_cars:
    print(True)
else:
    print(False)

if my_current_car not in john_cars:
    print(f'john has never owned {my_current_car}. But after our marriage he has')
    john_cars.append(my_current_car)
    print(john_cars)

# 5.3
# alien_color = ['green', 'yellow', 'red']
alien_color = 'green'

if 'green' in alien_color:
    print('You earned 5 points')

alien_color = 'red'

if 'green' in alien_color:
    print('You earned 5 points')

# 5.4
alien_color = 'green'

if 'lila' in alien_color:
    print('You earned 5 points')
else:
    print('You earned 10 points')

alien_color = 'green'

if 'lila' in alien_color:
    print('You earned 5 points')
if 'lila' not in alien_color:
    print('You earned 10 points')

# 5.5
alien_color = 'red'
points = []

if 'green' in alien_color:
    points = 5
elif 'yellow' in alien_color:
    points = 10
elif 'red' in alien_color:
    points = 15
print(f'You earned {points} points')

# 5.6
age = 65
value = []

if age < 2:
    value = 'infant'
elif age < 4:
    value = 'toddler'
elif age < 13:
    value = 'child'
elif age < 20:
    value = 'teenager'
elif age < 65:
    value = 'adult'
elif age >= 65:
    value = 'elderly'
print(value)


# 5.7
favorite_fruits = ['pineapple', 'watermelon', 'apple']
if 'banana' in favorite_fruits:
    print('You are really love banana')
if 'cherry' in favorite_fruits:
    print('You are really love cherry')
if 'apple' in favorite_fruits:
    print('You are really love apple')
if 'pineapple' in favorite_fruits:
    print('You are really love pineapple')
if 'watermelon' in favorite_fruits:
    print('You are really love watermelon')

# 5.8
print('\n5.8')
users = ['admin', 'martin', 'maria', 'john', 'markus']
for user in users:
    if user == 'admin':
        print(f'Hello {user.title()}, would you like to check journals?')
    else:
        print(f'Hello, {user.title()} thank you for logging again')

# 5.9
users = []
if users:
    for user in users:
        print()
else:
    print('empty')
# so ->
if users:
    for user in users:
        if user == 'admin':
            print(f'Hello {user.title()}, would you like to check journals?')
        else:
            print(f'Hello, {user.title()} thank you for logging again')
else:
    print('We need find some users')

# 5.10
print('\n5.10')
current_users = ['Admin', 'Martin', 'maria', 'JOHN', 'markus']
new_users = ['viola', 'martin', 'kevin', 'john', 'santos']
current_users_case_insensitive = [x.lower() for x in current_users]

for new_user in new_users:
    if new_user in current_users_case_insensitive:
        print(f'Sorry, name {new_user} is used. Choose another one')
    else:
        print(f'Name {new_user} is available. You can use it')

# 5.11
print('\n5.11')

numbers = []
for number in range(1, 10):
    numbers.append(number)

for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')
