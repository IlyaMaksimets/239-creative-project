import sys

import pygame

from grand_battle.Resources.CodeFragments.classes import Button
from grand_battle.Resources.CodeFragments.database_functions import update_settings
from grand_battle.Resources.CodeFragments.menu_functions import keybinding
from grand_battle.Resources.CodeFragments.other_functions import get_font


def options_keyboard(SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config):
    while True:
        options_mouse_pos = pygame.mouse.get_pos()

        SCREEN.fill("#121212")
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))
        return_to_main_menu_O = Button(data=CAV_config.data,
                                       image=pygame.image.load("Textures/return_button_disabled.png"),
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

        move_up_key = get_font(50).render("Up: " + CAV_config.keybinds["move_up"], True, "#b68f40")
        move_up_key_rect = move_up_key.get_rect(center=(1050, 150))
        SCREEN.blit(move_up_key, move_up_key_rect)

        move_down_key = get_font(50).render("Down: " + CAV_config.keybinds["move_down"], True, "#b68f40")
        move_down_key_rect = move_down_key.get_rect(center=(1050, 250))
        SCREEN.blit(move_down_key, move_down_key_rect)

        move_left_key = get_font(50).render("Left: " + CAV_config.keybinds["move_left"], True, "#b68f40")
        move_left_key_rect = move_left_key.get_rect(center=(1050, 350))
        SCREEN.blit(move_left_key, move_left_key_rect)

        move_right_key = get_font(50).render("Right: " + CAV_config.keybinds["move_right"], True, "#b68f40")
        move_right_key_rect = move_right_key.get_rect(center=(1050, 450))
        SCREEN.blit(move_right_key, move_right_key_rect)

        jump_key = get_font(50).render("Jump: " + CAV_config.keybinds["jump"], True, "#b68f40")
        jump_key_rect = jump_key.get_rect(center=(1050, 550))
        SCREEN.blit(jump_key, jump_key_rect)

        pause_key = get_font(50).render("Pause: " + CAV_config.keybinds["pause"], True, "#b68f40")
        pause_key_rect = pause_key.get_rect(center=(1050, 650))
        SCREEN.blit(pause_key, pause_key_rect)

        change_key_buttons = []

        for i in range(6):
            change_button = Button(data=CAV_config.data, image=pygame.image.load("Textures/change_button_disabled.png"),
                                   image_path="Textures/change_button_disabled.png", pos=(1550, i * 100 + 150))
            change_button.changeCondition(options_mouse_pos)
            change_button.update(SCREEN)
            change_key_buttons.append(change_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(6):
                    if change_key_buttons[i].checkForInput(options_mouse_pos):
                        MUSIC_config.button_click_sound.play()
                        MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                        if i == 0:
                            keybinding("move_up", SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                                       GROUPS_config)
                        if i == 1:
                            keybinding("move_down", SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                                       MAPS_config, GROUPS_config)
                        if i == 2:
                            keybinding("move_left", SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                                       MAPS_config, GROUPS_config)
                        if i == 3:
                            keybinding("move_right", SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                                       MAPS_config, GROUPS_config)
                        if i == 4:
                            keybinding("jump", SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                                       GROUPS_config)
                        if i == 5:
                            keybinding("pause", SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                                       GROUPS_config)

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
                    return ['options_video', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                            MAPS_config, GROUPS_config]

                if keyboard_button.checkForInput(options_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)

        pygame.display.update()
