"""
game_functions.py
This module stores useful functions for the Alien Invasion game
"""

import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_q: # Close the game with 'q' key
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_bullets(bullets):
    """Update bullet positions and remove exiting bullets""" 
    bullets.update()

    # Get rid of bullets that have exited the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom == 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Create a bullet and add it to the bullets group"""
    if len(bullets) < ai_settings.bullets_allowed: 
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    """Draw a fleet of aliens to fill the first screen row"""
    # Get number of aliens per row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space = ai_settings.screen_width - 2 * alien_width
    n_aliens_x = int(available_space / (1.8 * alien_width))
    
    # Create the first row of aliens
    for alien_number in range(0, n_aliens_x):
        # Create alien and place in on the row
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + alien_number * 1.8 * alien_width
        alien.rect.x = alien.x
        aliens.add(alien)


def update_screen(screen, settings, ship, aliens, bullets):
    """draw the current elements onscreen"""
    # Draw screen color and ship 
    screen.fill(settings.bg_color)
    ship.blitme()
    aliens.draw(screen)

    # Redraw all bullets in their current positions
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make the most recently drawn screen visible to user
    pygame.display.flip()
