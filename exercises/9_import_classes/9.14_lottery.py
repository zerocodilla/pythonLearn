from random import choice

numbers = []
for number in range(1,11):
    numbers.append(number)

numbers.append('a')
numbers.append('b')
numbers.append('c')
numbers.append('d')
numbers.append('e')

print(numbers)

ticket = []
value = 1
while value <= 4:
    value += 1
    ticket.append(choice(numbers))
print(f"The ticket with the following values wins: {ticket}")


