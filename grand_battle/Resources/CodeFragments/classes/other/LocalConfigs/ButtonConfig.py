import pygame


class ButtonConfig:
    def __init__(self):
        self.SCREEN_WIDTH = 1920
        self.SCREEN_HEIGHT = 1080
        self.SCREEN = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.PATH_INDENT = -12
        self.DESCRIPTION_FONT_SIZE = 10
        self.LEVEL_STATUS_FONT_SIZE = 24
