from random import sample

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_ticket = ['d', 2, 'b', 8]
ticket = []
attempt = 1

while ticket != my_ticket:
    ticket = sample(numbers, 4)
    attempt += 1

print(f"{attempt} attempts are required to win.")
print(ticket)
