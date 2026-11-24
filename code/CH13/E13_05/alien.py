"""
alien.py
Module that defines the Alien class
"""

import pygame

class Alien:
    def __init__(self, ss_settings, screen):
        """Initialize alien and set its starting position"""
        self.ss_settings = ss_settings
        self.screen = screen

        # Load the alien image and get its rect
        self.image = pygame.image.load("images/alien_archer.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start the alien at the center left of the sceeen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        # Store the center as float, to allow speed increments
        self.center = float(self.rect.centery) 

        # Flags for ship movement
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up:
            if self.rect.top > self.screen_rect.top:
                self.center -= self.ss_settings.alien_speed_factor
        if self.moving_down:
            if self.rect.bottom < self.screen_rect.bottom:
                self.center += self.ss_settings.alien_speed_factor
        self.rect.centery = self.center
