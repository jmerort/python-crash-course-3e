"""
shooter.py
Module that defines the Shooter class
"""

import pygame

class Shooter:
    def __init__(self, ss_game):
        """Initialize shooter and set its starting position"""
        self.settings = ss_game.settings
        self.screen = ss_game.screen

        # Load the shooter image and get its rect
        self.image = pygame.image.load("images/alien_archer.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start the shooter at the center left of the sceeen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        # Store the center as float, to allow speed increments
        self.center = float(self.rect.centery) 

        # Flags for ship movement
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw the shooter at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self, dt):
        if self.moving_up:
            if self.rect.top > self.screen_rect.top:
                self.center -= self.settings.shooter_speed_factor * dt
        if self.moving_down:
            if self.rect.bottom < self.screen_rect.bottom:
                self.center += self.settings.shooter_speed_factor * dt
        self.rect.centery = self.center
