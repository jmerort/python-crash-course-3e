"""
alien.py
Module that defines the Alien (enemy) class
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to represent a single alien of the fleet"""
    def __init__(self, ai_settings, screen):
        """Initialize alien and set its starting position"""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/alien.png")
        self.rect = self.image.get_rect()

        # Start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact position
        self.x = float(self.rect.x) 

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)
