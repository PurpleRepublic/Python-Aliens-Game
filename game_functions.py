import sys
import pygame
from bullet import Bullet
from alien import Alien

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
         fire_bullet(ai_settings,screen,ship,bullets)


def check_events(ai_settings,screen, ship, bullets):
    """Respond to keypresses and mouse movements"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                check_key_down_events(event,ai_settings,screen, ship, bullets)

            elif event.type == pygame.KEYUP:
                check_key_up_events(event,ship)

                
def update_screen(ai_settings,screen,ship, bullets, aliens):
    #Update images on the screen and flip to the new screen
    #Redrawing the screen during each pass through loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)

    #Redraw each all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #makeing the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """Update postion of bullets and get rid of old bullets."""
    #Update bullet postions.
    bullets.update()

    #Delete bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

def fire_bullet(ai_settings,screen,ship,bullets):
    """fires bullets, up to four on screen"""
    #Creat new bullet and add it to bullet group
    if len(bullets) <= ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen,ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """find number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determi the number of rows of aliens that fit on screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def creat_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    #Create an alien and find the number of aliens in a row.
    #Spacing between each alien is equal to the one alien width.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #Create fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """Drop aliens and send them other direction once edge has been reached"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the fleet and change it's deriction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens):
    """Update the postion of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()