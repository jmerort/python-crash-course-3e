"""
13-1
Stars: Find an image of a star. Make a grid of stars appear on the screen.

Nov 2026
@jmerort
"""

import sys

import pygame

from settings import Settings
from star import Star

class Stars():
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initilize the game and create game resources"""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0], pygame.FULLSCREEN | pygame.SCALED, vsync=1)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()
        self.create_constelation()

        # Set the background color
        self.bg_color = (230, 230, 230)


    def create_constelation(self):
        """Create a constelation of stars."""
        # Create n rows of stars
        star_width = Star(self).rect.width
        star_height = Star(self).rect.height

        current_y = star_height
        while current_y < self.settings.screen_height - 2 * star_height:
            current_x = star_width
            while current_x < self.settings.screen_width - star_width:
                self.create_star(current_x, current_y)
                current_x += 2 * star_width
            current_y += 2 * star_height


    def create_star(self, x, y):
        new_star = Star(self)
        new_star.x = x
        new_star.rect.x = x
        new_star.rect.y = y
        self.stars.add(new_star)


    def run_game(self):
        """Start the main loop for the game."""
        self.dt = 0

        while True:
            self.check_events()
            self.update_screen()
            self.dt = self.clock.tick(120) / 1000 # Get seconds since last frame


    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)


    def check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()


    def update_screen(self):
        """Update images onscreen and flip to a new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
            
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    """Make a game instance, and run the game."""
    s = Stars()
    s.run_game()
