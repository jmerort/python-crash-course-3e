"""
Alien Invasion.py

Main file of the game
"""

import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

class AlienInvasion():
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initilize the game and create game resources"""
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) # Give an AlienInvasion instane as arg

        # Set the background color
        self.bg_color = (230, 230, 230)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.check_events()
            self.ship.update()
            self.update_screen()
            self.clock.tick(60)


    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
           elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)


   def check_keydown_events(self):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True


    def check_keyup_events(self):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def update_screen(self):
        """Update images onscreen and flip to a new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    """Make a game instance, and run the game."""
    ai = AlienInvasion()
    ai.run_game()
