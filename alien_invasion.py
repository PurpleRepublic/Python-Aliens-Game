import sys 
import pygame 
from pygame.sprite import Group
from alien import Alien

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    #initializing game and creating string object
    pygame.init()
    ai_settings = Settings()
    screen= pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make play button
    play_button = Button(ai_settings, screen, "Play")

    #Create an instance to store game statistics
    stats = GameStats(ai_settings)

    #Make ship
    ship = Ship(ai_settings,screen)
    #Make a group to store bullets
    bullets = Group()
    #Make an alien
    aliens = Group()

    #Create alien fleet
    gf.create_fleet(ai_settings, screen,ship, aliens)

    #Starting main loop
    while True:

        #watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens,bullets)

        gf.update_screen(ai_settings,screen, stats, ship, bullets, aliens, play_button)


run_game()


