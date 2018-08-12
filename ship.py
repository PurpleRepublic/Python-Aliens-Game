import pygame

class Ship():
    def __init__(self,screen):
        """initialisation of ship and setting its start position"""
        self.screen = screen

        #load ship image and get rectangle form image"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect  = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draws the ship at it's current location."""
        self.screen.blit(self.image,self.rect)
