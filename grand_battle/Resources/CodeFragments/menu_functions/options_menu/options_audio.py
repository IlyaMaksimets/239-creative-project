import sys

import pygame

from Resources.CodeFragments.classes import Button


def options_audio(SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config):
    while True:

        options_mouse_pos = pygame.mouse.get_pos()

        SCREEN.fill("#121212")
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))
        return_to_main_menu_O = Button(image=pygame.image.load("../Textures/return_button_disabled.png"),
                                       image_path="../Textures/return_button_disabled.png", pos=(310, 900))

        return_to_main_menu_O.changeCondition(options_mouse_pos)
        return_to_main_menu_O.update(SCREEN)

        song_on_off_button = Button(image=pygame.image.load("../Textures/music_en_dis_button_disabled.png"),
                                    image_path="../Textures/music_en_dis_button_disabled.png", pos=(730, 300))
        song_on_off_button.changeCondition(options_mouse_pos)
        song_on_off_button.update(SCREEN)

        sounds_on_off_button = Button(image=pygame.image.load("../Textures/volume_en_dis_button_disabled.png"),
                                      image_path="../Textures/volume_en_dis_button_disabled.png", pos=(730, 600))
        sounds_on_off_button.changeCondition(options_mouse_pos)
        sounds_on_off_button.update(SCREEN)

        audio_button = Button(image=pygame.image.load("../Textures/audio_button_disabled.png"),
                              image_path="../Textures/audio_button_disabled.png", pos=(400, 200))
        audio_button.changeCondition(options_mouse_pos)
        audio_button.update(SCREEN)

        video_button = Button(image=pygame.image.load("../Textures/video_button_disabled.png"),
                              image_path="../Textures/video_button_disabled.png", pos=(400, 350))
        video_button.changeCondition(options_mouse_pos)
        video_button.update(SCREEN)

        keyboard_button = Button(image=pygame.image.load("../Textures/keyboard_button_disabled.png"),
                                 image_path="../Textures/keyboard_button_disabled.png", pos=(400, 500))
        keyboard_button.changeCondition(options_mouse_pos)
        keyboard_button.update(SCREEN)

        CAV_config.SONG_VOLUME_buttons = []
        for i in range(10):
            song_vol_button_condition = ""
            if CAV_config.data[i + 40][:2] == "of":
                song_vol_button_condition = "off"
            else:
                song_vol_button_condition = "on"
            CAV_config.SONG_VOLUME_button_path = "../Textures/volume_button_" + song_vol_button_condition + "_disabled.png"
            CAV_config.SONG_VOLUME_buttons.append(
                Button(image=pygame.image.load(CAV_config.SONG_VOLUME_button_path),
                       image_path=CAV_config.SONG_VOLUME_button_path,
                       pos=(1000 + i * 70, 300)))
        for i in range(10):
            CAV_config.SONG_VOLUME_buttons[i].changeCondition(options_mouse_pos)
            CAV_config.SONG_VOLUME_buttons[i].update(SCREEN)

        CAV_config.SOUNDS_VOLUME_buttons = []
        for i in range(10):
            sounds_vol_button_condition = ""
            if CAV_config.data[i + 51][:2] == "of":
                sounds_vol_button_condition = "off"
            else:
                sounds_vol_button_condition = "on"
            CAV_config.SOUNDS_VOLUME_button_path = "../Textures/volume_button_" + sounds_vol_button_condition + \
                                                   "_disabled.png"
            CAV_config.SOUNDS_VOLUME_buttons.append(
                Button(image=pygame.image.load(CAV_config.SOUNDS_VOLUME_button_path),
                       image_path=CAV_config.SOUNDS_VOLUME_button_path,
                       pos=(1000 + i * 70, 600)))
        for i in range(10):
            CAV_config.SOUNDS_VOLUME_buttons[i].changeCondition(options_mouse_pos)
            CAV_config.SOUNDS_VOLUME_buttons[i].update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_main_menu_O.checkForInput(options_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['main_menu', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                            MAPS_config, GROUPS_config]
                if song_on_off_button.checkForInput(options_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    if not CAV_config.SONG_VOLUME:
                        CAV_config.SONG_VOLUME = 10
                        CAV_config.data[40] = "on\n"
                    else:
                        CAV_config.SONG_VOLUME = 0
                        for i in range(40, 50):
                            CAV_config.data[i] = "off\n"

                if sounds_on_off_button.checkForInput(options_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    if not CAV_config.SOUNDS_VOLUME:
                        CAV_config.SOUNDS_VOLUME = 10
                        CAV_config.data[51] = "on\n"
                    else:
                        CAV_config.SOUNDS_VOLUME = 0
                        for i in range(51, 61):
                            CAV_config.data[i] = "off\n"

                for i in range(10):
                    if CAV_config.SONG_VOLUME_buttons[i].checkForInput(options_mouse_pos):
                        CAV_config.SONG_VOLUME = i * 10 + 10
                        MUSIC_config.button_click_sound.play()
                        MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                        for j in range(40, 41 + i):
                            CAV_config.data[j] = "on\n"
                        for j in range(41 + i, 50):
                            CAV_config.data[j] = "off\n"
                MUSIC_config.background_theme.set_volume(CAV_config.SONG_VOLUME / 100)

                for i in range(10):
                    if CAV_config.SOUNDS_VOLUME_buttons[i].checkForInput(options_mouse_pos):
                        CAV_config.SOUNDS_VOLUME = i * 10 + 10
                        MUSIC_config.button_click_sound.play()
                        MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                        for j in range(51, 52 + i):
                            CAV_config.data[j] = "on\n"
                        for j in range(52 + i, 61):
                            CAV_config.data[j] = "off\n"

                if audio_button.checkForInput(options_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)

                if video_button.checkForInput(options_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['options_video', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                            MAPS_config, GROUPS_config]

                if keyboard_button.checkForInput(options_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return ['options_keyboard', SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                            MAPS_config, GROUPS_config]

        pygame.display.update()
