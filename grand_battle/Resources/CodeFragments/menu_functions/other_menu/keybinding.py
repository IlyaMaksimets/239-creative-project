import pygame

from Resources.CodeFragments.classes import Button
from Resources.CodeFragments.database_functions import update_key_in_db
from Resources.CodeFragments.other_functions import get_font


def keybinding(action, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config):
    key_not_pressed = 1
    while key_not_pressed:

        options_mouse_pos = pygame.mouse.get_pos()

        SCREEN.fill("#121212")

        return_to_options_O = Button(image=pygame.image.load("../Textures/return_button_disabled.png"),
                                     image_path="../Textures/return_button_disabled.png", pos=(310, 900))

        return_to_options_O.changeCondition(options_mouse_pos)
        return_to_options_O.update(SCREEN)

        press_any_button = get_font(50).render("Press any button.", True, "#b68f40")
        press_any_button_rect = press_any_button.get_rect(center=(960, 450))
        SCREEN.blit(press_any_button, press_any_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_not_pressed = 0
                if event.key == pygame.K_a and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'A'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_b and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'B'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_c and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'C'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_d and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'D'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_e and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'E'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_f and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'F'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_g and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'G'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_h and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'H'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_i and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'I'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_j and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'J'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_k and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'K'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_l and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'L'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_m and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'M'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_n and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'N'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_o and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'O'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_p and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'P'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_q and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'Q'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_r and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'R'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_s and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'S'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_t and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'T'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_u and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'U'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_v and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'V'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_w and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'W'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_x and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'X'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_y and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'Y'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_z and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'Z'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_0 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = '0'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_1 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = '1'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_2 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = '2'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_3 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = '3'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_4 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = '4'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_5 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = '5'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_6 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = '6'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_7 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = '7'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_8 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = '8'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_9 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = '9'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_F1 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'F1'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_F2 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'F2'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_F3 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'F3'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_F4 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'F4'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_F5 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'F5'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_F6 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'F6'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_F7 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'F7'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_F8 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'F8'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_F9 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'F9'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_F10 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'F10'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_F11 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'F11'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_F12 and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'F12'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_SPACE and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'Space'
                    CAV_config.keyactions[action] = event.key
                if event.key == pygame.K_ESCAPE and (
                        event.key not in CAV_config.keyactions.values() or CAV_config.keyactions[action] == event.key):
                    CAV_config.keybinds[action] = 'esc'
                    CAV_config.keyactions[action] = event.key
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_options_O.checkForInput(options_mouse_pos):
                    MUSIC_config.button_click_sound.play()
                    MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    return SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config

        pygame.display.update()

    update_key_in_db(CAV_config.keybinds, action)
    return SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config
