import pygame


class GlobalGroupsConfig:
    def __init__(self):
        self.bullet_group = pygame.sprite.Group()
        self.enemy_bullet_group = pygame.sprite.Group()
        self.turret_group = pygame.sprite.Group()
        self.drop_crate_group = pygame.sprite.Group()
