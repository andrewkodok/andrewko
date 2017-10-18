import game_functions as gf
import pygame

from settings import Settings
from ship import Ship
from scoreboard import Scoreboard

from pygame.sprite import Group
from gamestats import GameStats
from button import Button

def run_game():
    # Initialize pygame, settings and a screen object.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((
        ai_settings.screen_width , ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion!")
    play_button = Button(ai_settings,screen,"Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    # Make a ship.
    ship = Ship(ai_settings,screen)

    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Starts the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, stats,sb, play_button, ship, aliens, bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
                         play_button)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)


        # Make the drawn screen visible.
        pygame.display.flip()

run_game()
