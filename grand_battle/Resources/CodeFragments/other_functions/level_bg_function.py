import pygame


def level_background(lvl_n, screen_scroll, CANVAS, SCREEN, MAP_MATRIX, wall_image, ladder_image):
    if lvl_n == 'endless':
        CANVAS.blit(pygame.image.load('../Textures/level_02.png'), (0, 0))
    else:
        CANVAS.blit(pygame.image.load('../Textures/level_0' + str(lvl_n) + '.png'), (0, 0))
        for i in range(22):
            for j in range(1, 8):
                CANVAS.blit(wall_image, (j * - 50 + screen_scroll, i * 50))
        for i in range(22):
            for j in range(1, 8):
                CANVAS.blit(wall_image, (5950 + j * 50 + screen_scroll, i * 50))
    for i in range(18):
        for j in range(len(MAP_MATRIX[i])):
            if MAP_MATRIX[i][j] == 'P' and (j * 50 + screen_scroll) in range(-200, 1800):
                CANVAS.blit(wall_image, (j * 50 + screen_scroll, i * 50))
            elif MAP_MATRIX[i][j] == 'L' and (j * 50 + screen_scroll) in range(-200, 1800):
                CANVAS.blit(ladder_image, (j * 50 + screen_scroll, i * 50))
    for i in range(4):
        for j in range(len(MAP_MATRIX[i])):
            if (j * 50 + screen_scroll) in range(-200, 1800):
                CANVAS.blit(wall_image, (j * 50 + screen_scroll, 900 + i * 50))

    SCREEN.blit(CANVAS, (240, 0))
