"""
12-5
Sideways Shooter: Write a game that places a ship on the left side of the
screen and allows the player to move the ship up and down. Make the ship fire
a bullet that travels right across the screen when the player presses the space-
bar. Make sure bullets are deleted once they disappear off the screen.

Nov 2026
@jmerort

Main file of the game.
I changed the ship for an alien I drew, to make it a bit different.
"""

import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from alien import Alien
import game_functions as gf

def run_game():
    """Initialize game and create a screen object"""
    pygame.init()

    ss_settings = Settings()

    screen = pygame.display.set_mode((ss_settings.screen_width, ss_settings.screen_height))
    pygame.display.set_caption("Sideways Shooter")
    
    # Make an alien
    alien = Alien(ss_settings, screen)
    # Make a group to store bullets in
    bullets = Group()

    # Start the main loop for the game
    while True:
        gf.check_events(ss_settings, screen, alien, bullets)
        alien.update()
        gf.update_bullets(bullets, screen)
        gf.update_screen(screen, ss_settings, alien, bullets)

run_game()
