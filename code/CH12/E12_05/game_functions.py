"""
game_functions.py
This module stores useful functions for the keys game
"""

import sys

import pygame

def check_events():
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            check_keydown_events(event)

        if event.type == pygame.KEYUP:
            check_keyup_events(event)


def check_keydown_events(event):
    print(f"Keydown event type : {event.key}.")

def check_keyup_events(event):
    print(f"Keyup event type : {event.key}.")

def update_screen(screen, settings):
    """draw the current elements onscreen"""
    # Draw screen color and ship 
    screen.fill(settings.bg_color)
    # Make the most recently drawn screen visible to user
    pygame.display.flip()
