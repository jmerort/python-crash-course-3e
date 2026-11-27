class GameStats():
    """
    Class for keeping statistics for the Sideways Shooter game.
    """
    def __init__(self, ss_game):
        self.settings = ss_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Bring the game stats to their default values."""
        self.shooter_lives = self.settings.shooter_lives
