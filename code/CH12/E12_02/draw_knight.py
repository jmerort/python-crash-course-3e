"""
12-2
Game Character: Find a bitmap image of a game character you like or
convert an image to a bitmap. Make a class that draws the character at the
center of the screen and match the background color of the image to the back-
ground color of the screen, or vice versa.

Nov 2026
@jmerort

Image by OpenClipart-Vectors, 
downloaded from https://pixabay.com/vectors/animal-horse-knight-mammal-rider-2023168/
The image is pretty big to be used as a game character, it should either be scaled
down or a smaller one should be used.
"""

import sys
import os

import pygame

class Knight():
    def __init__(self, screen):
        """Initialize knight and set its starting position"""
        self.screen = screen

        # Load image
        self.image = pygame.image.load(os.path.join("images", "knight.svg"))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the character at the rect location"""
        self.screen.blit(self.image, self.rect)

def draw_knight():
    """Draw a cool knight on horseback in the middle of the screen"""
    pygame.init()
    screen = pygame.display.set_mode((1400, 1000))
    pygame.display.set_caption("Game Character")

    bg_color = (150, 100, 100)

    knight = Knight(screen)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        knight.blitme()
        pygame.display.flip()

draw_knight()
