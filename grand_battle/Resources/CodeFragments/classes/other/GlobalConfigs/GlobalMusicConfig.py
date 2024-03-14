import pygame


class GlobalMusicConfig:
    def __init__(self):
        self.background_theme = pygame.mixer.Sound("Sounds/background_theme.mp3")
        self.button_click_sound = pygame.mixer.Sound("Sounds/button_click_sound.mp3")
        self.destruction_sound = pygame.mixer.Sound("Sounds/destruction_sound.mp3")
        self.game_over_sound = pygame.mixer.Sound("Sounds/game_over_sound.mp3")
        self.jump_sound = pygame.mixer.Sound("Sounds/jump_sound.mp3")
        self.shot_sound = pygame.mixer.Sound("Sounds/shot_sound.mp3")
        self.victory_sound = pygame.mixer.Sound("Sounds/victory_sound.mp3")
