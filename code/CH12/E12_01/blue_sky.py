"""
12-1
Blue Sky: Make a Pygame window with a blue background.

Nov 2026
@jmerort
"""

import sys

import pygame

def blue_sky():
    """Make a blue screen"""
    pygame.init()

    blue = (50, 180, 235)
    
    screen = pygame.display.set_mode((900, 900))
    pygame.display.set_caption("Blue Sky :-D")

    # Start game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(blue)
        pygame.display.flip()

blue_sky()
