"""
bullet class module for the Sideways Shooter game
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to mange bullets fired by the alien"""
    def __init__(self, ss_settings, screen, alien):
        """Create a bullet object at the alien's current position"""
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0,0) and then set its current position
        self.rect = pygame.Rect(0, 0, ss_settings.bullet_width, ss_settings.bullet_height)
        self.rect.centery = alien.rect.centery
        self.rect.right = alien.rect.right

        # Store bullet y position as decimal value
        self.x = self.rect.x

        self.color = ss_settings.bullet_color
        self.speed_factor = ss_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen"""
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw bullet onscreen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
