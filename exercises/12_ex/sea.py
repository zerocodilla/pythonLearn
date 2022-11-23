import sys
import pygame

from settings import Settings
from crab import Crab


class Sea:
    """Class to represent the sea and sea animals"""

    def __init__(self):
        """Class for resources management and game behaviour."""
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sea World")
        self.crab = Crab(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.crab.update()
            self.update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.crab.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.crab.moving_left = True
        elif event.key == pygame.K_UP:
            self.crab.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.crab.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.crab.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.crab.moving_left = False
        elif event.key == pygame.K_UP:
            self.crab.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.crab.moving_down = False

    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.screen_color)
        self.crab.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    sw = Sea()
    sw.run_game()
