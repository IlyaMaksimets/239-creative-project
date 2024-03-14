import pygame


class GlobalImagesConfig:
    def __init__(self):
        self.wall_image = pygame.image.load("Textures/ground_texture.png")
        self.ladder_image = pygame.image.load('Textures/ladder.png')
        self.turret_image = pygame.image.load('Textures/turret.png')
        self.l_1 = pygame.image.load('Textures/1_lives.png')
        self.l_2 = pygame.image.load('Textures/2_lives.png')
        self.l_3 = pygame.image.load('Textures/3_lives.png')
        self.l_4 = pygame.image.load('Textures/4_lives.png')
