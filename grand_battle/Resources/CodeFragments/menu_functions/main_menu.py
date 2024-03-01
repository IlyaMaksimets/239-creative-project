import sys

import pygame

from Resources.CodeFragments.database_functions import get_db_info, update_db
from Resources.CodeFragments.database_functions import keyconverting
from Resources.CodeFragments.classes import Button
from Resources.CodeFragments.other_functions import get_font


def main_menu(SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config):
    if CAV_config.first_launch:
        CAV_config.data, CAV_config.keybinds = get_db_info(CAV_config.keybinds)
        CAV_config.keyactions = keyconverting(CAV_config.keybinds, CAV_config.keyactions)

        for i in range(40, 50):
            if CAV_config.data[i][:2] == "on":
                CAV_config.SONG_VOLUME += 10

        for i in range(51, 61):
            if CAV_config.data[i][:2] == "on":
                CAV_config.SOUNDS_VOLUME += 10

        MUSIC_config.background_theme.play(-1)
        MUSIC_config.background_theme.set_volume(CAV_config.SONG_VOLUME / 100)
        CAV_config.first_launch = False

    while True:
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))

        SCREEN.fill("#121212")
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("GRAND BATTLE", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(960, 200))
        SCREEN.blit(menu_text, menu_rect)

        play_button = Button(image=pygame.image.load("../Textures/play_button_disabled.png"),
                             image_path="../Textures/play_button_disabled.png", pos=(960, 400))
        options_button = Button(image=pygame.image.load("../Textures/options_button_disabled.png"),
                                image_path="../Textures/options_button_disabled.png", pos=(960, 600))
        quit_button = Button(image=pygame.image.load("../Textures/quit_button_disabled.png"),
                             image_path="../Textures/quit_button_disabled.png", pos=(960, 800))

        for button in [play_button, options_button, quit_button]:
            button.changeCondition(menu_mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['play', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                            MAPS_config, GROUPS_config]
                if options_button.checkForInput(menu_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['options_audio', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                            MAPS_config, GROUPS_config]
                if quit_button.checkForInput(menu_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    CAV_config.data = update_db(CAV_config.data)
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


