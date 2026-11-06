"""
12-4
Keys: Make a Pygame file that creates an empty screen. In the event
loop, print the event.key attribute whenever a pygame.KEYDOWN event is detected.
Run the program and press various keys to see how Pygame responds.

Nov 2026
@jmerort

Main file of the game
"""

import sys

import pygame

from settings import Settings
import game_functions as gf

def run_game():
    """Initialize game and create a screen object"""
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Keys")
    
    # Start the main loop for the game
    while True:
        # Handle the event loop
        gf.check_events()

        # Update screen
        gf.update_screen(screen, ai_settings)

run_game()
