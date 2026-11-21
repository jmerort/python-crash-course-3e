"""
Alien Invasion.py

Main file of the game

NOTE: setting the framerate to 60 with clock.tick(60) as the book does,
made the ship movement wonky on my PC, so I enabled vsync to make the
game's framerate match my monitor's refresh rate and it worked better.
"""

import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion():
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

        # Set windowed mode at the resolution selected in settings.py
        #self.screen = pygame.display.set_mode(
        #        (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) # Give an AlienInvasion instane as arg
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.create_fleet()

        # Set the background color
        self.bg_color = (230, 230, 230)


    def create_fleet(self):
        """Create a fleet of aliens."""
        # Make an alien
        alien = Alien(self)
        self.aliens.add(alien)


    def run_game(self):
        """Start the main loop for the game."""
        self.dt = 0

        while True:
            self.check_events()
            self.ship.update(self.dt)
            self.update_bullets()
            self.update_screen()
            self.dt = self.clock.tick(120) / 1000 # Get seconds since last frame


    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)


    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self.fire_bullet()


    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def update_bullets(self):
        """Update the position of bullets and remove old bullets"""
        self.bullets.update(self.dt)

        # Check if any bullet has exited the screen and delete it.
        # Loop over a copy, because we are modyfying the list as we go along
        for bullet in self.bullets.copy(): 
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def update_screen(self):
        """Update images onscreen and flip to a new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
            
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    """Make a game instance, and run the game."""
    ai = AlienInvasion()
    ai.run_game()
