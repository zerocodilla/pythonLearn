class GameStats:
    """Stats for the game Alien Invasion."""

    def __init__(self, ai_game):
        """Initialise stats."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Game launches in the inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialise stats, changing during the game."""
        self.ships_left = self.settings.ship_limit