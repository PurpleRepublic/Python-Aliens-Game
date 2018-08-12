import sys 
import pygame 

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
    ship = Ship(screen)

    #Starting main loop
    while True:

        #watch for keyboard and mouse events
        gf.check_events()
        gf.update_screen(ai_settings,screen,ship)


run_game()


