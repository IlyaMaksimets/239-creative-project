import sys

import pygame

from grand_battle.Resources.CodeFragments.classes import Button
from grand_battle.Resources.CodeFragments.database_functions import update_settings
from grand_battle.Resources.CodeFragments.other_functions import get_font


def options_video(SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config):
    while True:

        options_mouse_pos = pygame.mouse.get_pos()

        SCREEN.fill("#121212")
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))
        return_to_main_menu_O = Button(data=CAV_config.data, image=pygame.image.load("Textures/return_button_disabled.png"),
                                       image_path="Textures/return_button_disabled.png", pos=(310, 900))

        return_to_main_menu_O.changeCondition(options_mouse_pos)
        return_to_main_menu_O.update(SCREEN)

        audio_button = Button(data=CAV_config.data, image=pygame.image.load("Textures/audio_button_disabled.png"),
                              image_path="Textures/audio_button_disabled.png", pos=(400, 200))
        audio_button.changeCondition(options_mouse_pos)
        audio_button.update(SCREEN)

        video_button = Button(data=CAV_config.data, image=pygame.image.load("Textures/video_button_disabled.png"),
                              image_path="Textures/video_button_disabled.png", pos=(400, 350))
        video_button.changeCondition(options_mouse_pos)
        video_button.update(SCREEN)

        keyboard_button = Button(data=CAV_config.data, image=pygame.image.load("Textures/keyboard_button_disabled.png"),
                                 image_path="Textures/keyboard_button_disabled.png", pos=(400, 500))
        keyboard_button.changeCondition(options_mouse_pos)
        keyboard_button.update(SCREEN)

        under_construction = get_font(50).render("Under construction.", True, "#b68f40")
        under_construction_rect = under_construction.get_rect(center=(1160, 450))
        SCREEN.blit(under_construction, under_construction_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_main_menu_O.checkForInput(options_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    update_settings(
                        {"song_volume": CAV_config.SONG_VOLUME, "sounds_volume": CAV_config.SOUNDS_VOLUME,
                         "move_left": CAV_config.keybinds["move_left"],
                         "move_right": CAV_config.keybinds["move_right"],
                         "move_up": CAV_config.keybinds["move_up"],
                         "move_down": CAV_config.keybinds["move_down"],
                         "jump": CAV_config.keybinds["jump"],
                         "pause": CAV_config.keybinds["pause"]})
                    return ['main_menu', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                            MAPS_config, GROUPS_config]

                if audio_button.checkForInput(options_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['options_audio', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                            MAPS_config, GROUPS_config]

                if video_button.checkForInput(options_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)

                if keyboard_button.checkForInput(options_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['options_keyboard', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                            MAPS_config, GROUPS_config]

        pygame.display.update()
