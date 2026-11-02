"""
Alien Invasion.py

Main file of the game
"""

import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    """Initialize game and create a screen object"""
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship
    ship = Ship(screen)

    # Start the main loop for the game
    while True:
        # Handle the event loop
        gf.check_events()
        
        # Update screen
        gf.update_screen(screen, ai_settings, ship)

run_game()
