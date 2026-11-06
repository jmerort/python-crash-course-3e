"""
12-3
Rocket: Make a game that begins with a rocket in the center of the
screen. Allow the player to move the rocket up, down, left, or right using the
four arrow keys. Make sure the rocket never moves beyond any edge of the
screen.

Nov 2026
@jmerort

Main file of the rocket game, a game about moving a rocket around the
screen. I reused the alien_invasion libraries, adding the movement parts
to ship.py and update_screen.py. 
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
    pygame.display.set_caption("Rocket Game")
    
    # Make a rocket
    rocket = Ship(ai_settings, screen)

    # Start the main loop for the game
    while True:
        # Handle the event loop
        gf.check_events(rocket)

        rocket.update()
        
        # Update screen
        gf.update_screen(screen, ai_settings, rocket)

run_game()
