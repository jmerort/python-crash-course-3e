"""
game_functions.py
This module stores useful functions for the Sideways Shooter game
"""

import sys

import pygame

from bullet import Bullet

def check_events(ss_settings, screen, alien, bullets):
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ss_settings, screen, alien, bullets)

        if event.type == pygame.KEYUP:
            check_keyup_events(event, alien)


def check_keydown_events(event, ss_settings, screen, alien, bullets):
    if event.key == pygame.K_UP:
        alien.moving_up = True
    if event.key == pygame.K_DOWN:
        alien.moving_down = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ss_settings, screen, alien, bullets)


def check_keyup_events(event, alien):
    if event.key == pygame.K_UP:
        alien.moving_up = False
    if event.key == pygame.K_DOWN:
        alien.moving_down = False


def update_bullets(bullets, screen):
    """Update bullet positions and remove exiting bullets""" 
    bullets.update()
    screen_rect = screen.get_rect()

    # Get rid of bullets that have exited the screen
    for bullet in bullets.copy():
        if bullet.rect.right == screen_rect.right:
            bullets.remove(bullet)


def fire_bullet(ss_settings, screen, alien, bullets):
    """Create a bullet and add it to the bullets group"""
    if len(bullets) < ss_settings.bullets_allowed: 
        new_bullet = Bullet(ss_settings, screen, alien)
        bullets.add(new_bullet)


def update_screen(screen, ss_settings, alien, bullets):
    """draw the current elements onscreen"""
    # Draw screen color and alien 
    screen.fill(ss_settings.bg_color)
    alien.blitme()

    # Redraw all bullets in their current positions
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make the most recently drawn screen visible to user
    pygame.display.flip()
