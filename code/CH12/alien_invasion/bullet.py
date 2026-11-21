"""
bullet class module for the Alien Invasion game
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to mange bullets fired from the ship"""
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect at (0,0) and then set its current position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.centerx = ai_game.ship.rect.centerx
        self.rect.top = ai_game.ship.rect.top

        # Store bullet y position as decimal value
        self.y = float(self.rect.y)


    def update(self, dt):
        """Move the bullet up the screen"""
        self.y -= self.settings.bullet_speed * dt
        self.rect.y = self.y


    def draw_bullet(self):
        """Draw bullet onscreen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
