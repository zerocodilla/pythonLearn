import pygame


class Ship:
    """A class representing a ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get its rect.
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's center.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # Ship settings
        self.ship_speed = 2

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ship_speed

        # Update rect object from self.center.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Place ship in the bottom center """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)