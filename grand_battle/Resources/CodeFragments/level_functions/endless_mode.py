import sys
from random import randint as rd

import pygame

from grand_battle.Resources.CodeFragments.classes import Button, Turret, Portal, DropCrate, EnemyBullet, Character, \
    EndlessModeConfig
from grand_battle.Resources.CodeFragments.database_functions import update_level
from grand_battle.Resources.CodeFragments.other_functions import get_font, level_background, endless_map_update


def add_turrets(GROUPS_config, MAPS_config, CAV_config):
    for i in range(18):
        for j in range(86):
            if MAPS_config.MAP_MATRIX[i][j] == '1':
                GROUPS_config.turret_group.add(
                    Turret(j * 50 + 290 + CAV_config.screen_scroll, i * 50 + 50, 3, 4, MAPS_config.MAP_MATRIX, 2))
    return GROUPS_config


def clear_groups(GROUPS_config):
    GROUPS_config.bullet_group.empty()
    GROUPS_config.enemy_bullet_group.empty()
    GROUPS_config.turret_group.empty()
    GROUPS_config.drop_crate_group.empty()


def initialize_pause_menu(SCREEN):
    pause_text = get_font(70).render("Game paused", True, "#b68f40")
    pause_rect = pause_text.get_rect(center=(960, 300))
    SCREEN.blit(pause_text, pause_rect)
    return Button(image=pygame.image.load("Textures/continue_button_disabled.png"),
                  image_path="Textures/continue_button_disabled.png", pos=(650, 700)), Button(
        image=pygame.image.load("Textures/restart_button_disabled.png"),
        image_path="Textures/restart_button_disabled.png", pos=(990, 700)), Button(
        image=pygame.image.load("Textures/exit_button_disabled.png"),
        image_path="Textures/exit_button_disabled.png", pos=(1330, 700))


def initialize_restart_menu():
    return Button(image=pygame.image.load("Textures/restart_button_disabled.png"),
                  image_path="Textures/restart_button_disabled.png", pos=(990, 700)), Button(
        image=pygame.image.load("Textures/exit_button_disabled.png"),
        image_path="Textures/exit_button_disabled.png", pos=(1330, 700))


def update_and_draw_game_objects(GROUPS_config, CAV_config, player, portal, change, SCREEN):
    player.draw()
    GROUPS_config.bullet_group.update(change, GROUPS_config.turret_group, player, CAV_config.screen_scroll)
    GROUPS_config.bullet_group.draw(SCREEN)
    GROUPS_config.enemy_bullet_group.update(change, player, CAV_config.screen_scroll)
    GROUPS_config.enemy_bullet_group.draw(SCREEN)
    GROUPS_config.drop_crate_group.draw(SCREEN)
    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
    pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))

    portal.update(change)
    portal.draw()


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
        q = rd(1, 100)
        if q <= 70:
            GROUPS_config.drop_crate_group.add(
                DropCrate(int(x), int(y), rd(1, 3), CAV_config.screen_scroll, rd(1, 2), MAPS_config.MAP_MATRIX))

    buffs = []
    for buff_crate in GROUPS_config.drop_crate_group:
        returned_data = buff_crate.update(change, player, CAV_config.screen_scroll)
        if returned_data is not None:
            buffs.append(returned_data)

    for i in buffs:
        player.realize_buff(i)


def spawn_turrets_player_and_portal(CAV_config, GROUPS_config, MAPS_config, Endless_mode_config, player):
    for i in range(18):
        for j in range(86):
            if MAPS_config.MAP_MATRIX[i][j] == '1' or (
                    MAPS_config.MAP_MATRIX[i][j] == '2' and CAV_config.TURRETS_DESTROYED_percentage >= 50) or (
                    MAPS_config.MAP_MATRIX[i][j] == '3' and CAV_config.TURRETS_DESTROYED_percentage >= 75):
                GROUPS_config.turret_group.add(
                    Turret(j * 50 + 290, i * 50 + 50, 3, 4, MAPS_config.MAP_MATRIX, 2))
                Endless_mode_config.turrets_spawned += 1
    player_lives = player.get_lives()
    player = Character(700, 770, 5, min(player_lives + 1, 4), MAPS_config.MAP_MATRIX, 0)
    portal = Portal(4495, 770, 'insane')
    portal.draw()
    return player


def handle_event_type_and_key(CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config, Endless_mode_config,
                              player,
                              SCREEN, CANVAS, clock):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == CAV_config.keyactions["move_left"]:
                Endless_mode_config.move_right = False
                Endless_mode_config.move_left = True
                player.ladder = False
                player.climbing = False
            if event.key == CAV_config.keyactions["move_right"]:
                Endless_mode_config.move_left = False
                Endless_mode_config.move_right = True
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

                    continue_button, retry_button, return_to_level_menu = initialize_pause_menu(SCREEN)
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
                            if return_to_level_menu.checkForInput(play_mouse_pos):
                                MUSIC_config.button_click_sound.play()
                                MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                                MUSIC_config.victory_sound.stop()
                                MUSIC_config.game_over_sound.stop()
                                return ['play', clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                                        MAPS_config, GROUPS_config]
                            if retry_button.checkForInput(play_mouse_pos):
                                MUSIC_config.button_click_sound.play()
                                MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                                MUSIC_config.victory_sound.stop()
                                MUSIC_config.game_over_sound.stop()
                                endless_mode(clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                                             MAPS_config,
                                             GROUPS_config)
                            if continue_button.checkForInput(play_mouse_pos):
                                paused = False

                    pygame.display.update()

            if event.key == CAV_config.keyactions[
                "move_up"] and not Endless_mode_config.move_left and not Endless_mode_config.move_right:
                player.climbing = True

        if event.type == pygame.KEYUP:
            if event.key == CAV_config.keyactions["move_left"]:
                Endless_mode_config.move_left = False
            if event.key == CAV_config.keyactions["move_right"]:
                Endless_mode_config.move_right = False
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
                         player, portal, Endless_mode_config):
    clock.tick(CAV_config.FPS)
    level_background(Endless_mode_config.level_num, player.get_screen_scroll(), CANVAS, SCREEN,
                     MAPS_config.MAP_MATRIX,
                     IMAGES_config.wall_image, IMAGES_config.ladder_image)
    change, CAV_config.GLOBAL_X = player.move(Endless_mode_config.move_left, Endless_mode_config.move_right,
                                              'endless')

    handle_returned_data(GROUPS_config, CAV_config, MAPS_config, change, player)

    update_and_draw_game_objects(GROUPS_config, CAV_config, player, portal, change, SCREEN)

    if not player.check_alive:
        Endless_mode_config.playing = False

    returned_list = handle_event_type_and_key(CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config,
                                              Endless_mode_config, player, SCREEN, CANVAS, clock)

    if returned_list is not None:
        return returned_list

    CAV_config.TURRETS_DESTROYED_percentage = CAV_config.TURRETS_DESTROYED / Endless_mode_config.turrets_spawned * 100

    if portal.check_completion(player):
        level_background(Endless_mode_config.level_num, player.get_screen_scroll(), CANVAS, SCREEN,
                         MAPS_config.MAP_MATRIX,
                         IMAGES_config.wall_image, IMAGES_config.ladder_image)
        clear_groups(GROUPS_config)
        MAPS_config.MAP_MATRIX, MAPS_config.MAP_SEGMENTS_NUMS = endless_map_update(MAPS_config.MAP_SEGMENTS_NUMS,
                                                                                   MAPS_config.MAP_SEGMENTS)

        player = spawn_turrets_player_and_portal(CAV_config, GROUPS_config, MAPS_config, Endless_mode_config, player)

    CAV_config.screen_scroll = player.get_screen_scroll()

    pygame.display.update()


def restart_menu_cycle_iteration(clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                                 GROUPS_config):
    play_mouse_pos = pygame.mouse.get_pos()

    retry_button, return_to_level_menu = initialize_restart_menu()
    retry_button.changeCondition(play_mouse_pos)
    retry_button.update(SCREEN)

    return_to_level_menu.changeCondition(play_mouse_pos)
    return_to_level_menu.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MUSIC_config.game_over_sound.stop()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if return_to_level_menu.checkForInput(play_mouse_pos):
                MUSIC_config.button_click_sound.play()
                MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                MUSIC_config.game_over_sound.stop()
                return ['play', clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                        MAPS_config, GROUPS_config]
            if retry_button.checkForInput(play_mouse_pos):
                MUSIC_config.button_click_sound.play()
                MUSIC_config.button_click_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
                MUSIC_config.game_over_sound.stop()
                endless_mode(SCREEN, clock, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config,
                             GROUPS_config)

    pygame.display.update()


def after_round_actions(CAV_config, MUSIC_config):
    MUSIC_config.game_over_sound.play()
    MUSIC_config.game_over_sound.set_volume(CAV_config.SOUNDS_VOLUME / 100)
    CAV_config.data[len(CAV_config.data) - 1] = str(
        max(int(CAV_config.data[len(CAV_config.data) - 1]), (CAV_config.GLOBAL_X + 500) // 50))
    update_level(
        {"time": f"00:00:00", "level": 0, "stars": CAV_config.data[len(CAV_config.data) - 1], "difficulty": 4})


def endless_mode(clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config):
    clear_groups(GROUPS_config)
    Endless_mode_config = EndlessModeConfig()
    CAV_config.TURRETS_DESTROYED, CAV_config.GLOBAL_X, CAV_config.screen_scroll, MAPS_config.MAP_SEGMENTS_NUMS = 0, -500, 0, [
        rd(0, 11), rd(0, 11), rd(0, 11)]
    player = Character(700, 770, 5, 4, MAPS_config.MAP_MATRIX, CAV_config.screen_scroll)
    portal = Portal(4495, 770, 'insane')
    MAPS_config.MAP_MATRIX, MAPS_config.MAP_SEGMENTS_NUMS = endless_map_update(MAPS_config.MAP_SEGMENTS_NUMS,
                                                                               MAPS_config.MAP_SEGMENTS)
    GROUPS_config = add_turrets(GROUPS_config, MAPS_config, CAV_config)

    while Endless_mode_config.playing:
        returned_list = game_cycle_iteration(clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                                             MAPS_config, GROUPS_config,
                                             player, portal, Endless_mode_config)
        if returned_list is not None:
            return returned_list

    after_round_actions(CAV_config, MUSIC_config)
    while True:
        returned_list = restart_menu_cycle_iteration(clock, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config,
                                                     MAPS_config,
                                                     GROUPS_config)
        if returned_list is not None:
            return returned_list
