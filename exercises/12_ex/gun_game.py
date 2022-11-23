import sys
import pygame
from gun import Gun
from settings import Settings
from bullet import Bullet


class GunGame:
    """Class for representing the gun game."""

    def __init__(self):
        """Initialize game and create resources for game."""
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Gun Game")
        self.bg_color = (230, 230, 230)
        self.gun = Gun(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.gun.update()
            self._update_bullets()
            self._update_screen()

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
        if event.key == pygame.K_UP:
            self.gun.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.gun.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.gun.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.gun.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and adding to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                 self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.gun.settings.bg_color)
        self.gun.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    # Create a game sample and run
    gg = GunGame()
    gg.run_game()
