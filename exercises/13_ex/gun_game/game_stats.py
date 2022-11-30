class GameStats:
    """Stats for the game Alien Invasion."""

    def __init__(self, ss_game):
        """Initialise stats."""
        self.settings = ss_game.settings
        self.reset_stats()
        # Game launches in the active state
        self.game_active = True

    def reset_stats(self):
        """Initialise stats, changing during the game."""
        self.ships_left = self.settings.ship_limit