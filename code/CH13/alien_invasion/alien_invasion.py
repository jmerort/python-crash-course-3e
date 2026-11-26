"""
Alien Invasion.py

Main file of the game

NOTE: setting the framerate to 60 with clock.tick(60) as the book does,
made the ship movement wonky on my PC, so I enabled vsync to make the
game's framerate match my monitor's refresh rate and it worked better.
"""

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
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

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self) # Give an AlienInvasion instane as arg
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.create_fleet()

        # Set the background color
        self.bg_color = (230, 230, 230)


    def create_fleet(self):
        """Create a fleet of aliens."""
        # Create n rows of aliens
        alien_width = Alien(self).rect.width
        alien_height = Alien(self).rect.height

        current_y = alien_height
        while current_y < self.settings.screen_height - 5 * alien_height:
            current_x = alien_width
            while current_x < self.settings.screen_width - 2 * alien_width:
                self.create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_y += 2 * alien_height


    def create_alien(self, x, y):
        new_alien = Alien(self)
        new_alien.x = x
        new_alien.rect.x = x
        new_alien.rect.y = y
        self.aliens.add(new_alien)


    def run_game(self):
        """Start the main loop for the game."""
        self.dt = 0

        while True:
            self.check_events()
            self.ship.update(self.dt)
            self.update_bullets()
            self.update_aliens()
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

        self.check_bullet_alien_collisions()


    def check_bullet_alien_collisions(self):
        """Respond to bullet allien collisions.""" 
        # Check for any bullets that have hit aliens.
        # If so, get rid of bullet and alien (True True arguments).
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        # Check if the fleet has been defeated.
        # If so, create new fleet.
        if not self.aliens:
            self.bullets.empty()
            self.create_fleet()


    def check_fleet_edges(self):
        """Check if any alien of the fleet has reacher either edge."""
        for alien in self.aliens:
            if alien.check_edges():
                self.change_fleet_direction()
                break


    def change_fleet_direction(self):
        """Drop down the fleet and change it's movement direction."""
        for alien in self.aliens:
            alien.rect.y += self.settings.fleet_drop_speed * self.dt
        self.settings.fleet_direction *= -1


    def update_aliens(self):
        """Update the position of each alien of the fleet."""
        self.aliens.update(self.dt)
        
        # Check for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()

        self.check_fleet_edges()


    def ship_hit(self):
        """Respond to the ship being hit by an alien."""
        # Decrement ships left.
        self.stats.ships_left -= 1

        # Get rid of remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        # Create new fleet and place the ship on the center.
        self.create_fleet()
        self.ship.center_ship()

        # Pause
        sleep(0.5)


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
