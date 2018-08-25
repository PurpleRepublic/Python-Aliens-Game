import sys
import pygame
from bullet import Bullet

def check_key_up_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_key_down_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
         #Creat new bullet and add it to bullet group
         new_bullet = Bullet(ai_settings, screen,ship)
         bullets.add(new_bullet)

def check_events(ai_settings,screen, ship, bullets):
    """Respond to keypresses and mouse movements"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                check_key_down_events(event,ai_settings,screen, ship, bullets)

            elif event.type == pygame.KEYUP:
                check_key_up_events(event,ship)
                
def update_screen(ai_settings,screen,ship, bullets):
    #Update images on the screen and flip to the new screen
    #Redrawing the screen during each pass through loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #Redraw each all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #makeing the most recently drawn screen visible
    pygame.display.flip()