import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent Aliens"""

    def __init__(self,ai_settings, screen):
        """Creat a alien object at top left of screen"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load alien image and get rectangle form image"""
        self.image = pygame.image.load('images/alien.bmp')
        self.rect  = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #create new ship at the top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien at starting location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move alien to the right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
