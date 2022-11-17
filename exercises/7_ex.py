# 7.1.
car = input("Which car do you want to rent? ")
print(f"Let me see if I can find you a {car.title()}")

# 7.2.
guests = input("How many people do you expect in your dinner group? ")
guests = int(guests)

if guests > 8:
    print("I am sorry. We need to ask you for waiting.")
else:
    print("Your table is ready. Follow me!")

# 7.3
number = input("Enter a number and I'll tell you if it is a multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")

# 7.4
prompt = 'Enter topping you want to add: '
prompt += "\nEnter 'quit' to send order. "
topping = ""

while topping != 'quit':
    topping = input(prompt)
    print(f"Adding {topping}")

# 7.5
# < 3 = free; < 12 = $10; >= 12 = $15

prompt = "How old are you? "
age = input(prompt)
age = int(age)

if age < 3:
    price = 0
elif age < 12:
    price = 10
else:
    price = 15
print(f"Your price is ${price}")

# 7.6
prompt = 'Enter topping you want to add: '
prompt += "\nEnter 'quit' to send order. "
active = True

while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"Adding {topping}")


# break
prompt = 'Enter topping you want to add: '
prompt += "\nEnter 'quit' to send order. "

while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping}")


# 7.7. infinite loop
#x = 9
#while x == 9:
#x    print(x)

# 7.8
sandwich_orders = ['tuna sandwich', 'ham sandwich', 'chicken sandwich', 'salmon sandwich']
finished_sandwich = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}")
    finished_sandwich.append(sandwich)
print(f"\nThe following sandwiches have been made:")
for sandwich in finished_sandwich:
    print(sandwich.title())

# 7.9
sandwich_orders = ['tuna sandwich', 'pastrami', 'ham sandwich', 'pastrami', 'chicken sandwich', 'pastrami', 'salmon']

print("I'm sorry. We are run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

# 7.10

users = {}

active = True

while active:
    name = input("Enter your name: ")
    response = input("Which country do you want to go for vacation? ")
    users[name] = response
    repeat = input("Would you like to let others to answer? yes/no ")
    if repeat == 'no':
        active = False

for name, response in users.items():
    print(f"\n{name.title()} would like to go to {response.title()}")
