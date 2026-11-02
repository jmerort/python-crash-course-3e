"""
game_functions.py
This module stores useful functions for the Alien Invasion game
"""

import sys

import pygame

def check_events():
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen, settings, ship):
    """draw the current elements onscreen"""
    # Draw screen color and ship 
    screen.fill(settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible to user
    pygame.display.flip()
