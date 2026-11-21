"""
star.py

Nov 2026
@jmerort
Module that defines the Star class (sprite made by me)
"""

import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """Class to represent a single star of the constelation."""
    def __init__(self, s_game):
        """Initialize star and set its starting position"""
        super().__init__()
        self.settings = s_game.settings
        self.screen = s_game.screen

        # Load the star image and get its rect
        self.image = pygame.image.load("images/star.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Start each star near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the star's exact position
        self.x = float(self.rect.x) 

    def blitme(self):
        """Draw the star at its current location"""
        self.screen.blit(self.image, self.rect)
