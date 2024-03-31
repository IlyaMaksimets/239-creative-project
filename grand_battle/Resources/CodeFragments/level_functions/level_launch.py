import sys
from random import randint as rd

import pygame

from grand_battle.Resources.CodeFragments.classes import Button, Turret, Portal, DropCrate, EnemyBullet, Character, \
    LevelLaunchConfig
from grand_battle.Resources.CodeFragments.database_functions import update_level
from grand_battle.Resources.CodeFragments.other_functions import get_font, load_map, level_background


def clear_groups(GROUPS_config):
    GROUPS_config.bullet_group.empty()
    GROUPS_config.enemy_bullet_group.empty()
    GROUPS_config.turret_group.empty()
    GROUPS_config.drop_crate_group.empty()


def initialize_difficulty_info(difficulty):
    if difficulty == 'beginner':
        return 1, 4, 2, 0
    if difficulty == 'medium':
        return 2, 3, 1, 1
    if difficulty == 'hard':
        return 3, 2, 4, 2
    if difficulty == 'insane':
        return 4, 1, 5, 3


def update_and_draw_game_objects(GROUPS_config, portal, player, SCREEN, change, CAV_config):
    portal.update(change)
    portal.draw()
    player.draw()
    GROUPS_config.bullet_group.update(change, GROUPS_config.turret_group, player, CAV_config.screen_scroll)
    GROUPS_config.bullet_group.draw(SCREEN)
    GROUPS_config.enemy_bullet_group.update(change, player, CAV_config.screen_scroll)
    GROUPS_config.enemy_bullet_group.draw(SCREEN)
    GROUPS_config.drop_crate_group.draw(SCREEN)
    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))


def set_c_d(difficulty):
    if difficulty == 'beginner':
        return 0
    if difficulty == 'medium':
        return 1
    if difficulty == 'hard':
        return 2
    if difficulty == 'insane':
        return 3


def set_total_time(ticks):
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 60)
    hours = int(ticks / 3600000 % 24)
    if seconds < 10:
        seconds = '0' + str(seconds)
    if minutes < 10:
        minutes = '0' + str(minutes)
    if hours < 10:
        hours = '0' + str(hours)

    return seconds, minutes, hours


def initialize_and_draw_pause_menu(SCREEN, CAV_config, after_death=False):
    if after_death:
        return Button(data=CAV_config.data, image=pygame.image.load("Textures/restart_button_disabled.png"),
                      image_path="Textures/restart_button_disabled.png", pos=(990, 700)), Button(data=CAV_config.data,
                                                                                                 image=pygame.image.load(
                                                                                                     "Textures/exit_button_disabled.png"),
                                                                                                 image_path="Textures/exit_button_disabled.png",
                                                                                                 pos=(1330, 700))

    pause_text = get_font(70).render("Game paused", True, "#b68f40")
    pause_rect = pause_text.get_rect(center=(960, 300))
    SCREEN.blit(pause_text, pause_rect)
    return Button(data=CAV_config.data, image=pygame.image.load("Textures/continue_button_disabled.png"),
                  image_path="Textures/continue_button_disabled.png", pos=(650, 700)), Button(data=CAV_config.data,
                                                                                              image=pygame.image.load(
                                                                                                  "Textures/restart_button_disabled.png"),
                                                                                              image_path="Textures/restart_button_disabled.png",
                                                                                              pos=(990, 700)), Button(
        data=CAV_config.data,
        image=pygame.image.load("Textures/exit_button_disabled.png"),
        image_path="Textures/exit_button_disabled.png", pos=(1330, 700))


def get_drop_chance(difficulty):
    if difficulty == 'beginner':
        return 100
    if difficulty == 'medium':
        return 70
    if difficulty == 'hard':
        return 30
    else:
        return 0


def add_turrets(GROUPS_config, MAPS_config, Level_launch_config, CAV_config):
    for i in range(18):
        for j in range(120):
            if MAPS_config.MAP_MATRIX[i][j] == 'T':
                GROUPS_config.turret_group.add(
                    Turret(j * 50 + 290, i * 50 + 50, Level_launch_config.TURRET_HEALTH,
                           Level_launch_config.BULLET_SPEED, MAPS_config.MAP_MATRIX, Level_launch_config.c_d,
                           CAV_config))
    return GROUPS_config


def handle_returned_data(GROUPS_config, CAV_config, MAPS_config, change, player):
    requests = []
    drop_crates = []
    for i in GROUPS_config.turret_group:
        returned_data = i.update(change, player)
        if returned_data is None:
            continue
        if len(returned_data) == 2:
            drop_crates.append((returned_data[0], returned_data[1]))
            CAV_config.TURRETS_DESTROYED += 1
        else:
            requests.append(returned_data)
    for request in requests:
        if request is None or len(request) < 4:
            continue
        GROUPS_config.enemy_bullet_group.add(
            EnemyBullet(int(request[0]), int(request[1]), int(request[2]), int(request[3]), MAPS_config.MAP_MATRIX,
                        CAV_config.screen_scroll))

    for x, y in drop_crates:
        if rd(1, 100) <= get_drop_chance(CAV_config.CHOSEN_DIFFICULTY):
            GROUPS_config.drop_crate_group.add(
                DropCrate(int(x), int(y), rd(1, 3), CAV_config.screen_scroll, rd(1, 2), MAPS_config.MAP_MATRIX))

    buffs = []
    for buff_crate in GROUPS_config.drop_crate_group:
        returned_data = buff_crate.update(change, player, CAV_config.screen_scroll)
        if returned_data is not None:
            buffs.append(returned_data)
    for i in buffs:
        player.realize_buff(i)


def handle_event_type_and_key(CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config, Level_launch_config,
                              player,
                              SCREEN, CANVAS, clock, level_num):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == CAV_config.keyactions["move_left"]:
                Level_launch_config.move_left = True
                Level_launch_config.move_right = False
                player.ladder = False
                player.climbing = False
            if event.key == CAV_config.keyactions["move_right"]:
                Level_launch_config.move_right = True
                Level_launch_config.move_left = False
                player.ladder = False
                player.climbing = False
            if event.key == CAV_config.keyactions["jump"] and not player.air:
                MUSIC_config.jump_sound.play()
                MUSIC_config.jump_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                player.jump = True
            if event.key == CAV_config.keyactions["pause"]:
                paused = True
                while paused:
                    play_mouse_pos = pygame.mouse.get_pos()

                    continue_button, retry_button, return_to_level_menu = initialize_and_draw_pause_menu(SCREEN,
                                                                                                         CAV_config)
                    continue_button.changeCondition(play_mouse_pos)
                    continue_button.update(SCREEN)
                    retry_button.changeCondition(play_mouse_pos)
                    retry_button.update(SCREEN)
                    return_to_level_menu.changeCondition(play_mouse_pos)
                    return_to_level_menu.update(SCREEN)

                    for sub_event in pygame.event.get():
                        if sub_event.type == pygame.QUIT:
                            MUSIC_config.victory_sound.stop()
                            MUSIC_config.game_over_sound.stop()
                            pygame.quit()
                            sys.exit()
                        if sub_event.type == pygame.MOUSEBUTTONDOWN:
                            if return_to_level_menu.checkForInput(play_mouse_pos) or retry_button.checkForInput(
                                    play_mouse_pos):
                                MUSIC_config.button_click_sound.play()
                                MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                                MUSIC_config.victory_sound.stop()
                                MUSIC_config.game_over_sound.stop()
                                if return_to_level_menu.checkForInput(play_mouse_pos):
                                    return ['play', clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                                            MAPS_config, GROUPS_config]
                                level_launch(level_num, clock, SCREEN, CANVAS, CAV_config, MUSIC_config,
                                             IMAGES_config,
                                             MAPS_config, GROUPS_config)

                            if continue_button.checkForInput(play_mouse_pos):
                                paused = False

                    pygame.display.update()

            if event.key == CAV_config.keyactions[
                "move_up"] and not Level_launch_config.move_left and not Level_launch_config.move_right:
                player.climbing = True

        if event.type == pygame.KEYUP:
            if event.key == CAV_config.keyactions["move_left"]:
                Level_launch_config.move_left = False
            if event.key == CAV_config.keyactions["move_right"]:
                Level_launch_config.move_right = False
            if event.key == CAV_config.keyactions["move_up"]:
                player.climbing = False

        if event.type == CAV_config.keyactions["shoot"]:
            if event.button == 1:
                if player.cooldown == 0:
                    player.cooldown = 30
                    MUSIC_config.shot_sound.play()
                    MUSIC_config.shot_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                    GROUPS_config.bullet_group.add(player.shoot())


def game_cycle_iteration(clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config,
                         player, portal, Level_launch_config, level_num):
    clock.tick(CAV_config.FPS)
    level_background(int(level_num), player.get_screen_scroll(), CANVAS, SCREEN, MAPS_config.MAP_MATRIX,
                     IMAGES_config.wall_image, IMAGES_config.ladder_image, 5950)
    change = player.move(Level_launch_config.move_left, Level_launch_config.move_right, 'level')

    handle_returned_data(GROUPS_config, CAV_config, MAPS_config, change, player)
    update_and_draw_game_objects(GROUPS_config, portal, player, SCREEN, change, CAV_config)

    if not player.check_alive:
        Level_launch_config.playing = False

    if portal.check_completion(player):
        Level_launch_config.playing = False
        Level_launch_config.completed = True
    returned_list = handle_event_type_and_key(CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config,
                                              Level_launch_config, player, SCREEN, CANVAS, clock, level_num)
    if returned_list is not None:
        return returned_list

    CAV_config.screen_scroll = player.get_screen_scroll()

    pygame.display.update()


def restart_menu_cycle_iteration(clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                                 GROUPS_config, level_num):
    play_mouse_pos = pygame.mouse.get_pos()

    retry_button, return_to_level_menu = initialize_and_draw_pause_menu(SCREEN, CAV_config, after_death=True)
    retry_button.changeCondition(play_mouse_pos)
    retry_button.update(SCREEN)
    return_to_level_menu.changeCondition(play_mouse_pos)
    return_to_level_menu.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MUSIC_config.victory_sound.stop()
            MUSIC_config.game_over_sound.stop()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if return_to_level_menu.checkForInput(play_mouse_pos) or retry_button.checkForInput(play_mouse_pos):
                MUSIC_config.button_click_sound.play()
                MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                MUSIC_config.victory_sound.stop()
                MUSIC_config.game_over_sound.stop()
                if return_to_level_menu.checkForInput(play_mouse_pos):
                    return ['play', clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                            GROUPS_config]
                level_launch(level_num, clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                             GROUPS_config)

    pygame.display.update()


def after_round_actions(CAV_config, MUSIC_config, Level_launch_config, level_num, clock1):
    ticks = pygame.time.get_ticks() - clock1
    seconds, minutes, hours = set_total_time(ticks)
    Level_launch_config.c_d = set_c_d(CAV_config.CHOSEN_DIFFICULTY)
    if Level_launch_config.completed:
        MUSIC_config.victory_sound.play()
        MUSIC_config.victory_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
        index = 62 + Level_launch_config.c_d * 36 + (int(level_num) - 1) * 4

        if CAV_config.TURRETS_DESTROYED in range(12, 15):
            if CAV_config.data[Level_launch_config.c_d * 10 + int(level_num) - 1][0] == '3':
                if int(CAV_config.data[index][:2]) * 3600 + int(
                        CAV_config.data[index + 1][:2]) * 60 + int(CAV_config.data[index + 2][:2]) > ticks / 1000:
                    write_time(CAV_config, seconds, minutes, hours, index)
                    update_level({"time": f"{hours}:{minutes}:{seconds}", "level": level_num, "stars": 3,
                                  "difficulty": Level_launch_config.c_d})
            else:
                write_time(CAV_config, seconds, minutes, hours, index)
                update_level({"time": f"{hours}:{minutes}:{seconds}", "level": level_num, "stars": 3,
                              "difficulty": Level_launch_config.c_d})
            CAV_config.data[Level_launch_config.c_d * 10 + int(level_num) - 1] = '3\n'

        elif CAV_config.TURRETS_DESTROYED in range(8, 12) and \
                CAV_config.data[Level_launch_config.c_d * 10 + int(level_num) - 1][0] != '3':
            if CAV_config.data[Level_launch_config.c_d * 10 + int(level_num) - 1][0] == '2':
                if int(CAV_config.data[index][:2]) * 3600 + int(
                        CAV_config.data[index + 1][:2]) * 60 + int(CAV_config.data[index + 2][:2]) > ticks / 1000:
                    write_time(CAV_config, seconds, minutes, hours, index)
                    update_level({"time": f"{hours}:{minutes}:{seconds}", "level": level_num, "stars": 2,
                                  "difficulty": Level_launch_config.c_d})
            else:
                write_time(CAV_config, seconds, minutes, hours, index)
                update_level({"time": f"{hours}:{minutes}:{seconds}", "level": level_num, "stars": 2,
                              "difficulty": Level_launch_config.c_d})
            CAV_config.data[Level_launch_config.c_d * 10 + int(level_num) - 1] = '2\n'

        elif CAV_config.TURRETS_DESTROYED in range(0, 8) and \
                CAV_config.data[Level_launch_config.c_d * 10 + int(level_num) - 1][
                    0] != '2' and \
                CAV_config.data[Level_launch_config.c_d * 10 + int(level_num) - 1][0] != '3':
            if CAV_config.data[Level_launch_config.c_d * 10 + int(level_num) - 1 + int(level_num)][0] == '1':
                if int(CAV_config.data[index][:2]) * 3600 + int(
                        CAV_config.data[index + 1][:2]) * 60 + int(CAV_config.data[index + 2][:2]) > ticks / 1000:
                    write_time(CAV_config, seconds, minutes, hours, index)
                    update_level({"time": f"{hours}:{minutes}:{seconds}", "level": level_num, "stars": 1,
                                  "difficulty": Level_launch_config.c_d})
            else:
                write_time(CAV_config, seconds, minutes, hours, index)
                update_level({"time": f"{hours}:{minutes}:{seconds}", "level": level_num, "stars": 1,
                              "difficulty": Level_launch_config.c_d})
            CAV_config.data[Level_launch_config.c_d * 10 + int(level_num) - 1] = '1\n'
    else:
        MUSIC_config.game_over_sound.play()
        MUSIC_config.game_over_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)


def write_time(CAV_config, seconds, minutes, hours, index):
    CAV_config.data[index] = str(hours) + '\n'
    CAV_config.data[index + 1] = str(minutes) + '\n'
    CAV_config.data[index + 2] = str(seconds) + '\n'


def get_portal_y(MAPS_config):
    for i in range(1, 16):
        if MAPS_config.MAP_MATRIX[i + 2][117] == 'P':
            return i * 50 + 20


def level_launch(level_num, clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config):
    Level_launch_config = LevelLaunchConfig()
    CAV_config.screen_scroll = 0
    CAV_config.TURRETS_DESTROYED = 0
    clear_groups(GROUPS_config)

    Level_launch_config.TURRET_HEALTH, Level_launch_config.CHARACTER_HEALTH, Level_launch_config.BULLET_SPEED, Level_launch_config.c_d = initialize_difficulty_info(
        CAV_config.CHOSEN_DIFFICULTY)

    MAPS_config.MAP_MATRIX = load_map(level_num)

    player = Character(700, 770, CAV_config.CHARACTER_SPEED, Level_launch_config.CHARACTER_HEALTH,
                       MAPS_config.MAP_MATRIX,
                       CAV_config.screen_scroll)

    Level_launch_config.portal_y = get_portal_y(MAPS_config)

    portal = Portal(6150, Level_launch_config.portal_y, CAV_config.CHOSEN_DIFFICULTY)
    clock1 = pygame.time.get_ticks()

    GROUPS_config = add_turrets(GROUPS_config, MAPS_config, Level_launch_config, CAV_config)

    while Level_launch_config.playing:
        returned_list = game_cycle_iteration(clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                                             MAPS_config, GROUPS_config,
                                             player, portal, Level_launch_config, level_num)
        if returned_list is not None:
            return returned_list

    after_round_actions(CAV_config, MUSIC_config, Level_launch_config, level_num, clock1)
    while True:
        returned_list = restart_menu_cycle_iteration(clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                                                     MAPS_config,
                                                     GROUPS_config, level_num)
        if returned_list is not None:
            return returned_list
