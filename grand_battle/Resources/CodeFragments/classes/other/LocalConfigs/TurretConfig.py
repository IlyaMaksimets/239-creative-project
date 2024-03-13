import pygame
from grand_battle.Resources.CodeFragments.database_functions import get_settings


class TurretConfig:
    def __init__(self):
        self.SCREEN_WIDTH = 1920
        self.SCREEN_HEIGHT = 1080
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.CHARACTER_SPEED = 5
        self.TURRETS_DESTROYED = 0
        res = get_settings({})
        self.SONG_VOLUME, self.SOUNDS_VOLUME = res["song_volume"], res["sounds_volume"]
