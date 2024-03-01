import pygame
from .classes import GlobalMusicConfig, GlobalImagesConfig, GlobalConstAndVarConfig
from .classes import GlobalMapsConfig, GlobalGroupsConfig, Menu


pygame.init()

CAV_config = GlobalConstAndVarConfig()
MUSIC_config = GlobalMusicConfig()
IMAGES_config = GlobalImagesConfig()
MAPS_config = GlobalMapsConfig()
GROUPS_config = GlobalGroupsConfig()


SCREEN = pygame.display.set_mode((CAV_config.SCREEN_WIDTH, CAV_config.SCREEN_HEIGHT))
CANVAS = pygame.Surface((CAV_config.SCREEN_WIDTH * 3, CAV_config.SCREEN_HEIGHT))


def main():
    menu = Menu(SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config)
    menu.main_menu_transition()


if __name__ == '__main__':
    main()
