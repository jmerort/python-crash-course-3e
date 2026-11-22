class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 20, 35)
        # Ship settings
        self.ship_speed = 300 # speed in pixels/second
        # Bullet settings
        self.bullet_speed = 400
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (190, 60, 60)
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed = 150
