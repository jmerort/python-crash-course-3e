"""
13-3
Raindrops: Find an image of a raindrop and create a grid of raindrops.
Make the raindrops fall toward the bottom of the screen until they disappear.

Nov 2026
@jmerort
"""

import sys

import pygame

from settings import Settings
from drop import Drop

class Raindrops():
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initilize the game and create game resources"""
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Set fullscreen with vsync governing framerate
        self.screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0], pygame.FULLSCREEN | pygame.SCALED, vsync=1)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Raindrops")

        self.drops = pygame.sprite.Group()
        self.create_rain()


    def create_rain(self):
        """Create a bunch of raindrops."""
        # Create n rows of drops
        drop_width = Drop(self).rect.width
        drop_height = Drop(self).rect.height

        current_y = drop_height
        while current_y < self.settings.screen_height - 5 * drop_height:
            current_x = drop_width
            while current_x < self.settings.screen_width - 2 * drop_width:
                self.create_drop(current_x, current_y)
                current_x += 2 * drop_width
            current_y += 2 * drop_height


    def create_drop(self, x, y):
        new_drop = Drop(self)
        new_drop.y = y
        new_drop.rect.x = x
        new_drop.rect.y = y
        self.drops.add(new_drop)


    def run_game(self):
        """Start the main loop for the game."""
        self.dt = 0

        while True:
            self.check_events()
            self.update_drops()
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


    def update_drops(self):
        """Update the position of each drop of the rain."""
        self.drops.update(self.dt)


    def update_screen(self):
        """Update images onscreen and flip to a new screen."""
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)
            
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    """Make a game instance, and run the game."""
    rain = Raindrops()
    rain.run_game()
