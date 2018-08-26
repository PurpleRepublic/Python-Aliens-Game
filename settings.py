class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        self.ship_speed_factor = 1.5

        #Bullet Settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        #Alien Settigns
        self.alien_speed_factor = .5
        self.fleet_drop_speed = 10
        #flieet_direction of 1 represents right; -1 is left.
        self.fleet_direction = 1