from random import choice

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
# combinations = len(numbers) ** len(my_ticket)
my_ticket = ['d', 10, 'a', 5]
result = []
attempt = 0

while True:
    while len(result) != len(my_ticket):
        result.append(choice(numbers))
    if my_ticket != result:
        result = []
        attempt += 1
    else:
        print(f"It's required {attempt} to win.")
        break

print(result)
