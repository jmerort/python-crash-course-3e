"""
sideways_shooter.py

Main file of the game. In this game, you must defend yourself from incoming 
enemies, which appear randomly on the right side of the screen.

Nov 2026
@jmerort
"""

import sys
from random import randint

import pygame

from settings import Settings
from shooter import Shooter
from bullet import Bullet
from enemy import Enemy

class SidewaysShooter():
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

        pygame.display.set_caption("Sideways Shooter")

        self.shooter = Shooter(self) # Give a Sideways Shooter instance as arg
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()


    def create_enemies(self):
        """
        Create enemies at random heights on the right side of 
        the screen, until there are as many as specified in settings.
        """
        enemy_width = Enemy(self).rect.width
        enemy_height = Enemy(self).rect.height
        
        n_enemies_current = len(self.enemies)
        current_x = self.settings.screen_width - enemy_width
        while(n_enemies_current < self.settings.n_enemies):
            current_y = (randint(0, self.settings.screen_height - enemy_height))
            self.create_enemy(current_x, current_y)
            n_enemies_current += 1


    def create_enemy(self, x, y):
        new_enemy = Enemy(self)
        new_enemy.x = x
        new_enemy.rect.x = x
        new_enemy.rect.y = y
        self.enemies.add(new_enemy)


    def run_game(self):
        """Start the main loop for the game."""
        self.dt = 0

        while True:
            self.check_events()
            self.shooter.update(self.dt)
            self.update_bullets()
            self.update_enemies()
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
        if event.key == pygame.K_UP:
            self.shooter.moving_up = True
        if event.key == pygame.K_DOWN:
            self.shooter.moving_down = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self.fire_bullet()


    def check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.shooter.moving_up = False
        if event.key == pygame.K_DOWN:
            self.shooter.moving_down = False


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
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)

        self.check_bullet_enemy_collisions()


    def check_bullet_enemy_collisions(self):
        """Respond to bullet allien collisions.""" 
        # Check for any bullets that have hit enemies.
        # If so, get rid of bullet and enemy (True True arguments).
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.enemies, True, True)


    def update_enemies(self):
        """Update the position of each enemy of the fleet."""
        self.enemies.update(self.dt)
        self.create_enemies()


    def update_screen(self):
        """Update images onscreen and flip to a new screen."""
        self.screen.fill(self.settings.bg_color)
        self.shooter.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.enemies.draw(self.screen)
            
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    """Make a game instance, and run the game."""
    ss = SidewaysShooter()
    ss.run_game()
