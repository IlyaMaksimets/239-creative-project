import sys

import pygame

from Resources.CodeFragments.classes import Button
from Resources.CodeFragments.menu_functions.other_menu.difficulty_list import difficulty_list
from Resources.CodeFragments.database_functions import get_db_info_WOquery5


def play(SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config):
    info_updated = False
    while True:
        chosen_diff = 0
        if CAV_config.CHOSEN_DIFFICULTY == 'beginner':
            chosen_diff = 0
        if CAV_config.CHOSEN_DIFFICULTY == 'medium':
            chosen_diff = 1
        if CAV_config.CHOSEN_DIFFICULTY == 'hard':
            chosen_diff = 2
        if CAV_config.CHOSEN_DIFFICULTY == 'insane':
            chosen_diff = 3

        play_mouse_pos = pygame.mouse.get_pos()

        SCREEN.fill("#121212")
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))

        CAV_config.levels_page_forward_button = Button(
            image=pygame.image.load("../Textures/forward_list_button_disabled.png"),
            image_path="../Textures/forward_list_button_disabled.png", pos=CAV_config.OOB)

        CAV_config.levels_page_forward_button.changeCondition(play_mouse_pos)
        CAV_config.levels_page_forward_button.update(SCREEN)

        CAV_config.levels_page_back_button = Button(
            image=pygame.image.load("../Textures/back_list_button_disabled.png"),
            image_path="../Textures/back_list_button_disabled.png", pos=CAV_config.OOB)

        CAV_config.levels_page_back_button.changeCondition(play_mouse_pos)
        CAV_config.levels_page_back_button.update(SCREEN)

        if CAV_config.levels_page == 1:
            CAV_config.levels_page_forward_button = Button(
                image=pygame.image.load("../Textures/forward_list_button_disabled.png"),
                image_path="../Textures/forward_list_button_disabled.png", pos=(1400, 500))

            CAV_config.levels_page_forward_button.changeCondition(play_mouse_pos)
            CAV_config.levels_page_forward_button.update(SCREEN)

        else:
            CAV_config.levels_page_back_button = Button(
                image=pygame.image.load("../Textures/back_list_button_disabled.png"),
                image_path="../Textures/back_list_button_disabled.png", pos=(1320, 500))

            CAV_config.levels_page_back_button.changeCondition(play_mouse_pos)
            CAV_config.levels_page_back_button.update(SCREEN)

        choose_difficulty = Button(
            image=pygame.image.load("../Textures/Difficulty buttons/difficulty_button_disabled.png"),
            image_path="../Textures/Difficulty buttons/difficulty_button_disabled.png", pos=(1500, 200))

        choose_difficulty.changeCondition(play_mouse_pos)
        choose_difficulty.update(SCREEN)

        level01_button_path = "../Textures/Level buttons/level01_button_stars-" + CAV_config.data[chosen_diff * 10][
            0] + "_disabled.png"
        level01_button_pos = CAV_config.OOB
        if CAV_config.levels_page == 1:
            level01_button_pos = (400, 300)
        level01_button = Button(image=pygame.image.load(level01_button_path), image_path=level01_button_path,
                                pos=level01_button_pos, level_button=1)
        if not info_updated:
            CAV_config.data = get_db_info_WOquery5()

        level01_button.changeCondition(play_mouse_pos, CHOSEN_DIFFICULTY=CAV_config.CHOSEN_DIFFICULTY)
        level01_button.update(SCREEN)

        level02_button_path = "../Textures/Level buttons/level02_button_stars-" + CAV_config.data[chosen_diff * 10 + 1][
            0] + "_disabled.png"
        level02_button_pos = CAV_config.OOB
        if CAV_config.levels_page == 1:
            level02_button_pos = (750, 300)
        level02_button = Button(image=pygame.image.load(level02_button_path), image_path=level02_button_path,
                                pos=level02_button_pos, level_button=2)
        if not info_updated:
            CAV_config.data = get_db_info_WOquery5()

        level02_button.changeCondition(play_mouse_pos, CHOSEN_DIFFICULTY=CAV_config.CHOSEN_DIFFICULTY)
        level02_button.update(SCREEN)

        level03_button_path = "../Textures/Level buttons/level03_button_stars-" + CAV_config.data[chosen_diff * 10 + 2][
            0] + "_disabled.png"
        level03_button_pos = CAV_config.OOB
        if CAV_config.levels_page == 1:
            level03_button_pos = (1100, 300)
        level03_button = Button(image=pygame.image.load(level03_button_path), image_path=level03_button_path,
                                pos=level03_button_pos, level_button=3)
        if not info_updated:
            CAV_config.data = get_db_info_WOquery5()

        level03_button.changeCondition(play_mouse_pos, CHOSEN_DIFFICULTY=CAV_config.CHOSEN_DIFFICULTY)
        level03_button.update(SCREEN)

        level04_button_path = "../Textures/Level buttons/level04_button_stars-" + CAV_config.data[chosen_diff * 10 + 3][
            0] + "_disabled.png"
        level04_button_pos = CAV_config.OOB
        if CAV_config.levels_page == 1:
            level04_button_pos = (400, 650)
        level04_button = Button(image=pygame.image.load(level04_button_path), image_path=level04_button_path,
                                pos=level04_button_pos, level_button=4)
        if not info_updated:
            CAV_config.data = get_db_info_WOquery5()

        level04_button.changeCondition(play_mouse_pos, CHOSEN_DIFFICULTY=CAV_config.CHOSEN_DIFFICULTY)
        level04_button.update(SCREEN)

        level05_button_path = "../Textures/Level buttons/level05_button_stars-" + CAV_config.data[chosen_diff * 10 + 4][
            0] + "_disabled.png"
        level05_button_pos = CAV_config.OOB
        if CAV_config.levels_page == 1:
            level05_button_pos = (750, 650)
        level05_button = Button(image=pygame.image.load(level05_button_path), image_path=level05_button_path,
                                pos=level05_button_pos, level_button=5)
        if not info_updated:
            CAV_config.data = get_db_info_WOquery5()

        level05_button.changeCondition(play_mouse_pos, CHOSEN_DIFFICULTY=CAV_config.CHOSEN_DIFFICULTY)
        level05_button.update(SCREEN)

        level06_button_path = "../Textures/Level buttons/level06_button_stars-" + CAV_config.data[chosen_diff * 10 + 5][
            0] + "_disabled.png"
        level06_button_pos = CAV_config.OOB
        if CAV_config.levels_page == 1:
            level06_button_pos = (1100, 650)
        level06_button = Button(image=pygame.image.load(level06_button_path), image_path=level06_button_path,
                                pos=level06_button_pos, level_button=6)
        if not info_updated:
            CAV_config.data = get_db_info_WOquery5()

        level06_button.changeCondition(play_mouse_pos, CHOSEN_DIFFICULTY=CAV_config.CHOSEN_DIFFICULTY)
        level06_button.update(SCREEN)

        level07_button_path = "../Textures/Level buttons/level07_button_stars-" + CAV_config.data[chosen_diff * 10 + 6][
            0] + "_disabled.png"
        level07_button_pos = CAV_config.OOB
        if CAV_config.levels_page == 2:
            level07_button_pos = (400, 300)
        level07_button = Button(image=pygame.image.load(level07_button_path), image_path=level07_button_path,
                                pos=level07_button_pos, level_button=7)
        if not info_updated:
            CAV_config.data = get_db_info_WOquery5()

        level07_button.changeCondition(play_mouse_pos, CHOSEN_DIFFICULTY=CAV_config.CHOSEN_DIFFICULTY)
        level07_button.update(SCREEN)

        level08_button_path = "../Textures/Level buttons/level08_button_stars-" + CAV_config.data[chosen_diff * 10 + 7][
            0] + "_disabled.png"
        level08_button_pos = CAV_config.OOB
        if CAV_config.levels_page == 2:
            level08_button_pos = (750, 300)
        level08_button = Button(image=pygame.image.load(level08_button_path), image_path=level08_button_path,
                                pos=level08_button_pos, level_button=8)
        if not info_updated:
            CAV_config.data = get_db_info_WOquery5()

        level08_button.changeCondition(play_mouse_pos, CHOSEN_DIFFICULTY=CAV_config.CHOSEN_DIFFICULTY)
        level08_button.update(SCREEN)

        level09_button_path = "../Textures/Level buttons/level09_button_stars-" + CAV_config.data[chosen_diff * 10 + 8][
            0] + "_disabled.png"
        level09_button_pos = CAV_config.OOB
        if CAV_config.levels_page == 2:
            level09_button_pos = (1100, 300)
        level09_button = Button(image=pygame.image.load(level09_button_path), image_path=level09_button_path,
                                pos=level09_button_pos, level_button=9)

        level09_button.changeCondition(play_mouse_pos, CHOSEN_DIFFICULTY=CAV_config.CHOSEN_DIFFICULTY)
        level09_button.update(SCREEN)
        if not info_updated:
            CAV_config.data = get_db_info_WOquery5()

        endless_button_path = "../Textures/endless_mode_button_disabled.png"
        endless_button = Button(image=pygame.image.load(endless_button_path), image_path=endless_button_path,
                                pos=(1490, 830), endless_button=1)

        endless_button.changeCondition(play_mouse_pos)
        endless_button.update(SCREEN)

        return_to_main_menu_P = Button(image=pygame.image.load("../Textures/return_button_disabled.png"),
                                       image_path="../Textures/return_button_disabled.png", pos=(310, 900))

        return_to_main_menu_P.changeCondition(play_mouse_pos)
        return_to_main_menu_P.update(SCREEN)

        info_updated = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_main_menu_P.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['main_menu', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                            GROUPS_config]

                if CAV_config.levels_page_forward_button.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    CAV_config.levels_page = 2
                if CAV_config.levels_page_back_button.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    CAV_config.levels_page = 1

                if choose_difficulty.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    returned_list = difficulty_list(return_to_main_menu_P, SCREEN, CANVAS, CAV_config, MUSIC_config,
                                                    IMAGES_config, MAPS_config, GROUPS_config)
                    if len(returned_list) == 1:
                        CAV_config.CHOSEN_DIFFICULTY = returned_list[0]
                    else:
                        return ['main_menu', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                                GROUPS_config]

                if level01_button.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['level_launch', '1', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                            GROUPS_config]
                if level02_button.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['level_launch', '2', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                            GROUPS_config]
                if level03_button.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['level_launch', '3', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                            GROUPS_config]
                if level04_button.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['level_launch', '4', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                            GROUPS_config]
                if level05_button.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['level_launch', '5', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                            GROUPS_config]
                if level06_button.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['level_launch', '6', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                            GROUPS_config]
                if level07_button.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['level_launch', '7', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                            GROUPS_config]
                if level08_button.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['level_launch', '8', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                            GROUPS_config]
                if level09_button.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['level_launch', '9', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                            GROUPS_config]

                if endless_button.checkForInput(play_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['endless_mode', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                            GROUPS_config]
        pygame.display.update()
