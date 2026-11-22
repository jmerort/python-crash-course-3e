"""
drop.py
Module that defines the Drop class
"""

import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
    """Class to represent a single drop of the rain"""
    def __init__(self, rain_game):
        """Initialize drop and set its starting position"""
        super().__init__()
        self.settings = rain_game.settings
        self.screen = rain_game.screen

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/drop.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Start each drop near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the drop's exact position
        self.y = float(self.rect.y) 

    def blitme(self):
        """Draw the drop at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self, dt):
        """Move the drop a set amount down."""
        self.y += self.settings.drop_speed * dt
        self.rect.y = self.y
