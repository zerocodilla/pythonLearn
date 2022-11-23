import pygame


class Crab:
    """Class to represent a sea animal."""

    def __init__(self, sw_game):
        """Initialize the crab and set its starting position."""
        self.screen = sw_game.screen
        self.settings = sw_game.settings
        self.screen_rect = sw_game.screen.get_rect()

        # Load crab image and get its rect.
        self.image = pygame.image.load('crab.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ship's center.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.speed = 1.5

    def update(self):
        """Update the position based on the movement flag."""
        # Update the crab's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed


        # Update rect object from self.center.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the crab at its current location."""
        self.screen.blit(self.image, self.rect)
