import sys 
import pygame 
from pygame.sprite import Group
from alien import Alien

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initializing game and creating string object
    pygame.init()
    ai_settings = Settings()
    screen= pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make ship
    ship = Ship(ai_settings,screen)
    #Make a group to store bullets
    bullets = Group()
    #Make an alien
    aliens = Group()

    #Create alien fleet
    gf.creat_fleet(ai_settings, screen,ship, aliens)

    #Starting main loop
    while True:

        #watch for keyboard and mouse events
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)


run_game()


