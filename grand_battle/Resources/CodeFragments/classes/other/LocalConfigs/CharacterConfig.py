import pygame
from grand_battle.Resources.CodeFragments.database_functions import get_settings


class CharacterConfig:
    def __init__(self):
        self.SCREEN_WIDTH = 1920
        self.SCREEN_HEIGHT = 1080
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.G = 0.5
        self.GLOBAL_X = -500
        self.CHARACTER_SPEED = 5
        self.l_1 = pygame.image.load('Textures/1_lives.png')
        self.l_2 = pygame.image.load('Textures/2_lives.png')
        self.l_3 = pygame.image.load('Textures/3_lives.png')
        self.l_4 = pygame.image.load('Textures/4_lives.png')
        self.CHOSEN_DIFFICULTY = 'beginner'
        res = get_settings({})
        self.SONG_VOLUME, self. SOUNDS_VOLUME = 0, 0
        if res is not None:
            self.SONG_VOLUME, self.SOUNDS_VOLUME = res["song_volume"], res["sounds_volume"]
