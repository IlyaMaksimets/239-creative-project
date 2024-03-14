import sys

import pygame

from grand_battle.Resources.CodeFragments.database_functions import keyconverting
from grand_battle.Resources.CodeFragments.classes import Button
from grand_battle.Resources.CodeFragments.other_functions import get_font
from grand_battle.Resources.CodeFragments.database_functions import get_data_and_keys


def login_menu(SCREEN):
    login_input_box = pygame.Rect(100, 100, 140, 32)
    password_input_box = pygame.Rect(100, 150, 140, 32)
    font = pygame.font.Font(None, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    login_box_color = color_inactive
    password_box_color = color_inactive
    login_box_active = False
    password_box_active = False
    login_text = ''
    password_text = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if login_input_box.collidepoint(event.pos):
                    login_box_active = not login_box_active
                else:
                    login_box_active = False
                if password_input_box.collidepoint(event.pos):
                    password_box_active = not password_box_active
                else:
                    password_box_active = False
                login_box_color = color_active if login_box_active else color_inactive
                password_box_color = color_active if password_box_active else color_inactive
            if event.type == pygame.KEYDOWN:
                if login_box_active:
                    if event.key == pygame.K_RETURN:
                        print(login_text)
                        login_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        login_text = login_text[:-1]
                    else:
                        login_text += event.unicode
                if password_box_active:
                    if event.key == pygame.K_RETURN:
                        print(password_text)
                        password_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        password_text = password_text[:-1]
                    else:
                        password_text += event.unicode

        SCREEN.fill((30, 30, 30))
        login_txt_surface = font.render(login_text, True, login_box_color)
        password_txt_surface = font.render(password_text, True, password_box_color)
        width = max(200, login_txt_surface.get_width() + 10)
        login_input_box.w = width
        password_input_box.w = width
        SCREEN.blit(login_txt_surface, (login_input_box.x + 5, login_input_box.y + 5))
        pygame.draw.rect(SCREEN, login_box_color, login_input_box, 2)
        SCREEN.blit(password_txt_surface, (password_input_box.x + 5, password_input_box.y + 5))
        pygame.draw.rect(SCREEN, password_box_color, password_input_box, 2)

        pygame.display.update()


def main_menu(SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config):
    token = open("token.txt", 'r').readlines()[0]
    if len(token) < 20:
        login_menu(SCREEN)
    if CAV_config.first_launch:
        CAV_config.data, CAV_config.keybinds = get_data_and_keys({})
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

        play_button = Button(image=pygame.image.load("Textures/play_button_disabled.png"),
                             image_path="Textures/play_button_disabled.png", pos=(960, 400))
        options_button = Button(image=pygame.image.load("Textures/options_button_disabled.png"),
                                image_path="Textures/options_button_disabled.png", pos=(960, 600))
        quit_button = Button(image=pygame.image.load("Textures/quit_button_disabled.png"),
                             image_path="Textures/quit_button_disabled.png", pos=(960, 800))

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
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


