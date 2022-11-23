class Settings:
    """A class to store all settings for Gun Game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bullet_speed = 1
        self.bullet_width = 7
        self.bullet_height = 7
        self.bullet_color = (255, 64, 64)
        self.bullets_allowed = 3