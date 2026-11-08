"""
settings.py
Settings for the game alien invasion
"""

class Settings():
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (180, 160, 100)
        # Alien settings
        self.alien_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_height = 6
        self.bullet_width = 30
        self.bullet_color = (120, 60, 120)
        self.bullets_allowed = 5
