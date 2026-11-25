"""
enemy.py
Module that defines the Enemy class. The enemies are 
desert creatures that start at the right side of the screen and 
move left towards the shooter.
"""

import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, ss_game):
        """Initialize enemy and set its starting position"""
        super().__init__()
        self.settings = ss_game.settings
        self.screen = ss_game.screen

        # Load the enemy image and get its rect
        self.image = pygame.image.load("images/desert_enemy.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start the enemy at the center right of the sceeen
        self.rect.centery = self.screen_rect.centery
        self.rect.x = self.screen_rect.x
        # Store the center as float, to allow speed increments
        self.x = float(self.rect.x) 


    def blitme(self):
        """Draw the enemy at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self, dt):
        self.x -= self.settings.enemy_speed_factor * dt
        self.rect.x = self.x
