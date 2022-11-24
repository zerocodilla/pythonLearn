import sys
import pygame
from stars import Star
from random import randint


class StarsSky:
    """Class for resources management and game behaviour."""

    def __init__(self):
        """Initialize game and create resources for game."""
        self.screen_height = 800
        self.screen_width = 1200
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Stars Sky")
        self.screen_color = (72, 61, 139)
        self.stars = pygame.sprite.Group()
        self._create_stars()

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_stars(self):
        """Create sky with stars."""
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)
        # Define available rows
        available_space_y = (self.screen_height - (2 * star_height))
        number_rows = available_space_y // (2 * star_height)
        # Create fleet of aliens.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create a star and find the number of stars in a row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.rect.x = star_width + 3 * star_width * star_number
        star.rect.y = star.rect.height + 3 * star.rect.height * row_number

        # Randomize star position
        star.rect.x += randint(-20, 20)
        star.rect.y += randint(-15, 15)

        self.stars.add(star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.screen_color)
        self.stars.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    sh = StarsSky()
    sh.run_game()
