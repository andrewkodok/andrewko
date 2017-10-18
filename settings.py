class Settings():

       """A class to store all settings for Alien Invasion."""

       def __init__(self):
           """Initialize the game's settings."""

           # Screen settings

           self.screen_width = 1000
           self.screen_height = 600
           self.bg_color = (230, 230, 230)
           self.ship_speed_factor = 3.0
           self.ship_limit = 3

           # Bullet settings

           self.bullet_speed_factor = 100
           self.bullet_width = 4
           self.bullet_height = 40
           self.bullet_color = (77,199,200)
           self.bullets_allowed = 5

           # Alien settings
           self.alien_speed_factor = 70
           self.fleet_drop_speed = 20

           #fleet_direction of 1 = right, -1 = left

           self.fleet_direction = 1

           # How quickly the game speeds up
           self.speedup_scale = 1.1

           # How quickly the alien point values increase
           self.score_scale = 1.5

           self.initialize_dynamic_settings()

       def initialize_dynamic_settings(self):
           self.ship_speed_factor = 3
           self.bullet_speed_factor = 7
           self.alien_speed_factor = 2
           self.fleet_direction = 1
           self.alien_points = 50

       def increase_speed(self):
           self.ship_speed_factor *= self.speedup_scale
           self.bullet_speed_factor *= self.speedup_scale
           self.alien_speed_factor *= self.speedup_scale
           self.alien_points = int(self.alien_points * self.score_scale)
           print(self.alien_points)





