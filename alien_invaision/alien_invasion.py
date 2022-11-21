import sys

import pygame
from settings import Settings
from ship import Ship
from planet import Planet


class AlienInvasion:
    """Class for resources management and game behaviour."""

    def __init__(self):
        """Initialize game and create resources for game."""
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # Make a ship
        self.ship = Ship(self)
        # Add a planet
        self.planet = Planet(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.planet.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # Create a game sample and run
    ai = AlienInvasion()
    ai.run_game()

