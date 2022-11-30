import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1800
        self.screen_height = 1000
        self.bg = pygame.image.load('images/bg.png')
        self.bullet_speed = 2.0
        self.bullet_width = 7
        self.bullet_height = 20
        self.bullet_color = (255, 193, 37)
        self.bullets_allowed = 3
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.alien_frequency = 0.008
        self.alien_speed = 50
        self.ship_limit = 3
