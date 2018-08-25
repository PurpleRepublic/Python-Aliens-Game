import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """initialisation of ship and setting its start position"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load ship image and get rectangle form image"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect  = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's postition based on the movement flag"""
        #update ships center value. not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left: #0 would  also work
            self.center -= self.ai_settings.ship_speed_factor

        #update rect object form self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draws the ship at it's current location."""
        self.screen.blit(self.image,self.rect)
