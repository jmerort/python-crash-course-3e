"""
bullet class module for the Sideways Shooter game
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to mange bullets fired by the shooter"""
    def __init__(self, ss_game):
        """Create a bullet object at the self.shooter's current position"""
        super().__init__()
        self.settings = ss_game.settings
        self.screen = ss_game.screen 
        self.shooter = ss_game.shooter

        # Create a bullet rect at (0,0) and then set its current position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.centery = self.shooter.rect.centery
        self.rect.right = self.shooter.rect.right

        # Store bullet y position as decimal value
        self.x = self.rect.x

        self.color = self.settings.bullet_color
        self.speed_factor = self.settings.bullet_speed_factor

    def update(self, dt):
        """Move the bullet up the screen"""
        self.x += self.speed_factor * dt
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw bullet onscreen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
