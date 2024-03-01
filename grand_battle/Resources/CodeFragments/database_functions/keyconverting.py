import pygame


def keyconverting(keybinds, keyactions):
    for action in keybinds:
        if keybinds[action] == 'A':
            keyactions[action] = pygame.K_a
        if keybinds[action] == 'B':
            keyactions[action] = pygame.K_b
        if keybinds[action] == 'C':
            keyactions[action] = pygame.K_c
        if keybinds[action] == 'D':
            keyactions[action] = pygame.K_d
        if keybinds[action] == 'E':
            keyactions[action] = pygame.K_e
        if keybinds[action] == 'F':
            keyactions[action] = pygame.K_f
        if keybinds[action] == 'G':
            keyactions[action] = pygame.K_g
        if keybinds[action] == 'H':
            keyactions[action] = pygame.K_h
        if keybinds[action] == 'I':
            keyactions[action] = pygame.K_i
        if keybinds[action] == 'J':
            keyactions[action] = pygame.K_j
        if keybinds[action] == 'K':
            keyactions[action] = pygame.K_k
        if keybinds[action] == 'L':
            keyactions[action] = pygame.K_l
        if keybinds[action] == 'M':
            keyactions[action] = pygame.K_m
        if keybinds[action] == 'N':
            keyactions[action] = pygame.K_n
        if keybinds[action] == 'O':
            keyactions[action] = pygame.K_o
        if keybinds[action] == 'P':
            keyactions[action] = pygame.K_p
        if keybinds[action] == 'Q':
            keyactions[action] = pygame.K_q
        if keybinds[action] == 'R':
            keyactions[action] = pygame.K_r
        if keybinds[action] == 'S':
            keyactions[action] = pygame.K_s
        if keybinds[action] == 'T':
            keyactions[action] = pygame.K_t
        if keybinds[action] == 'U':
            keyactions[action] = pygame.K_u
        if keybinds[action] == 'V':
            keyactions[action] = pygame.K_v
        if keybinds[action] == 'W':
            keyactions[action] = pygame.K_w
        if keybinds[action] == 'X':
            keyactions[action] = pygame.K_x
        if keybinds[action] == 'Y':
            keyactions[action] = pygame.K_y
        if keybinds[action] == 'Z':
            keyactions[action] = pygame.K_z
        if keybinds[action] == '1':
            keyactions[action] = pygame.K_1
        if keybinds[action] == '2':
            keyactions[action] = pygame.K_2
        if keybinds[action] == '3':
            keyactions[action] = pygame.K_3
        if keybinds[action] == '4':
            keyactions[action] = pygame.K_4
        if keybinds[action] == '5':
            keyactions[action] = pygame.K_5
        if keybinds[action] == '6':
            keyactions[action] = pygame.K_6
        if keybinds[action] == '7':
            keyactions[action] = pygame.K_7
        if keybinds[action] == '8':
            keyactions[action] = pygame.K_8
        if keybinds[action] == '9':
            keyactions[action] = pygame.K_9
        if keybinds[action] == '0':
            keyactions[action] = pygame.K_0
        if keybinds[action] == 'F1':
            keyactions[action] = pygame.K_F1
        if keybinds[action] == 'F2':
            keyactions[action] = pygame.K_F2
        if keybinds[action] == 'F3':
            keyactions[action] = pygame.K_F3
        if keybinds[action] == 'F4':
            keyactions[action] = pygame.K_F4
        if keybinds[action] == 'F5':
            keyactions[action] = pygame.K_F5
        if keybinds[action] == 'F6':
            keyactions[action] = pygame.K_F6
        if keybinds[action] == 'F7':
            keyactions[action] = pygame.K_F7
        if keybinds[action] == 'F8':
            keyactions[action] = pygame.K_F8
        if keybinds[action] == 'F9':
            keyactions[action] = pygame.K_F9
        if keybinds[action] == 'F10':
            keyactions[action] = pygame.K_F10
        if keybinds[action] == 'F11':
            keyactions[action] = pygame.K_F11
        if keybinds[action] == 'F12':
            keyactions[action] = pygame.K_F12
        if keybinds[action] == 'Space':
            keyactions[action] = pygame.K_SPACE
        if keybinds[action] == 'esc':
            keyactions[action] = pygame.K_ESCAPE
        if keybinds[action] == 'LMB':
            keyactions[action] = pygame.MOUSEBUTTONDOWN

    return keyactions
