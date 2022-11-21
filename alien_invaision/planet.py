import pygame


class Planet:
    """A class represent a planet."""

    def __init__(self, ai_game):
        """Initialize the planet and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load planet image and get its rect.
        self.image = pygame.image.load('images/galaxy.png')
        self.rect = self.image.get_rect()

        # Display the planet in the upper right corner of the screen.
        self.rect.topright = self.screen_rect.topright

    def blitme(self):
        """Draw the planet at its current location."""
        self.screen.blit(self.image, self.rect)
