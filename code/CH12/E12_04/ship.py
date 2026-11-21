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
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start the ship at the bottom centre of the sceeen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # Store the center as float, to allow speed increments
        self.centerx = float(self.rect.centerx) 
        self.centery = float(self.rect.centery) 

        # Flags for ship movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """Update rocket position based on state of movement"""
        if self.moving_right:
            if self.rect.right < self.screen_rect.right:
                self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left:
            if self.rect.left > self.screen_rect.left:
                self.centerx -= self.ai_settings.ship_speed_factor
        # As top of screen is Y=0, to move up, Y must decrease
        if self.moving_up:
            if self.rect.top > self.screen_rect.top: 
                self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down:
            if self.rect.bottom < self.screen_rect.bottom:
                self.centery += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
