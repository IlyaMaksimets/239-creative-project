import sys

import pygame

from grand_battle.Resources.CodeFragments.classes import Button


def difficulty_list(return_to_main_menu_P, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                    GROUPS_config):
    while True:
        diffculty_list_mouse_pos = pygame.mouse.get_pos()

        return_to_main_menu_P.changeCondition(diffculty_list_mouse_pos)
        return_to_main_menu_P.update(SCREEN)

        beginner_difficulty = Button(data=CAV_config.data,
            image=pygame.image.load("Textures/Difficulty buttons/beginner_difficulty_button_disabled.png"),
            image_path="Textures/Difficulty buttons/beginner_difficulty_button_disabled.png", pos=(1500, 300),
            difficulty_button=1)

        beginner_difficulty.changeCondition(diffculty_list_mouse_pos)
        beginner_difficulty.update(SCREEN)

        medium_difficulty = Button(data=CAV_config.data,
            image=pygame.image.load("Textures/Difficulty buttons/medium_difficulty_button_disabled.png"),
            image_path="Textures/Difficulty buttons/medium_difficulty_button_disabled.png", pos=(1500, 400),
            difficulty_button=2)

        medium_difficulty.changeCondition(diffculty_list_mouse_pos)
        medium_difficulty.update(SCREEN)

        hard_difficulty = Button(data=CAV_config.data,
            image=pygame.image.load("Textures/Difficulty buttons/hard_difficulty_button_disabled.png"),
            image_path="Textures/Difficulty buttons/hard_difficulty_button_disabled.png", pos=(1500, 500),
            difficulty_button=3)

        hard_difficulty.changeCondition(diffculty_list_mouse_pos)
        hard_difficulty.update(SCREEN)

        insane_difficulty = Button(data=CAV_config.data,
            image=pygame.image.load("Textures/Difficulty buttons/insane_difficulty_button_disabled.png"),
            image_path="Textures/Difficulty buttons/insane_difficulty_button_disabled.png", pos=(1500, 600),
            difficulty_button=4)

        insane_difficulty.changeCondition(diffculty_list_mouse_pos)
        insane_difficulty.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_main_menu_P.checkForInput(diffculty_list_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    return ['main_menu', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                            GROUPS_config]
                if beginner_difficulty.checkForInput(diffculty_list_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['beginner']
                if medium_difficulty.checkForInput(diffculty_list_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['medium']
                if hard_difficulty.checkForInput(diffculty_list_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['hard']
                if insane_difficulty.checkForInput(diffculty_list_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['insane']
        pygame.display.update()
