import pygame


class Gun:
    """A gun representing a ship."""

    def __init__(self, gg_game):
        """Initialize the ship and set its starting position."""
        self.screen = gg_game.screen
        self.settings = gg_game.settings
        self.screen_rect = gg_game.screen.get_rect()

        # Load ship image and get its rect.
        self.image = pygame.image.load('gun.png')
        self.rect = self.image.get_rect()

        # Start each new gun at the left in the middle.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's center.
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

        # Ship settings
        self.speed = 1.5

    def update(self):
        """Update the position based on the movement flag."""
        # Update the crab's center value, not the rect.
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        # Update rect object from self.center.
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
