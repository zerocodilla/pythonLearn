import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """Class representing one star."""

    def __init__(self, sh_game):
        """Initialise a star and set its current position."""
        super().__init__()
        self.screen = sh_game.screen

        # Load alien picture and set rect atribute.
        self.image = pygame.image.load('star.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)


