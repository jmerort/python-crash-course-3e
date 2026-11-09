"""
ship.py
Module that defines the Ship class
"""

import pygame

class Ship:
    def __init__(self, ai_settings, screen):
        """Initialize ship and set its starting position"""
        self.ai_settings = ai_settings
        self.screen = screen

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start the ship at the bottom centre of the sceeen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Store the center as float, to allow speed increments
        self.center = float(self.rect.centerx) 

        # Flags for ship movement
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            if self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            if self.rect.left > self.screen_rect.left:
                self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
