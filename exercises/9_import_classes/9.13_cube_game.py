from random import randint


class Cube:
    """Represent cube."""

    def __init__(self, slides=6):
        """Initialize cube."""
        self.slides = slides

    def roll_cube(self):
        """Return random number from 1 to number of slides."""
        message = randint(1, self.slides)
        print(message)


cube_0 = Cube()
attempt = 1
while attempt <= 10:
    attempt += 1
    cube_0.roll_cube()

cube_1 = Cube(10)
attempt = 1
while attempt <= 10:
    attempt += 1
    cube_1.roll_cube()

cube_2 = Cube(20)
attempt = 1
while attempt <= 10:
    attempt += 1
    cube_2.roll_cube()



