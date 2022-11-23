import sys
import pygame


class Screen:
    """Class to represent a screen"""

    def __init__(self):
        """Initialize a screen."""
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_color = (232, 232, 112)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""

        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()


    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.screen_color)
        pygame.display.flip()

if __name__ == '__main__':
    kg = Screen()
    kg.run_game()
