import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Start the ship at the bottom centre of the sceeen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a float for the ship's horizontal position."""
        self.x = float(self.rect.x)

        # Movement flag. Start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)


    def update(self, dt):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed * dt
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed * dt
        
        self.rect.x = round(self.x)
