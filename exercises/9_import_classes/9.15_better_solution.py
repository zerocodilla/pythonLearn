from random import choice


class Lottery:

    def __init__(self, *win_lot):
        self.win_lot = win_lot

    def win_ticket(self):
        tries_0 = 1
        win_ticket = []
        while tries_0 <= 4:
            win_ticket.append(choice(self.win_lot))
            tries_0 += 1
        return win_ticket


l = Lottery('a', 'b', 'c', 'd', 'g', 2, 4, 5, 6, 1, 6, 7, 9, 2, 6)
my_ticket = [5, 'a', 2, 1]

tries_1 = 1
while True:
    current = l.win_ticket()
    print(f'current: {current}')
    if current == my_ticket:
        break
    tries_1 += 1

print(f'tries: {tries_1}')
