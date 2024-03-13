import pygame

from grand_battle.Resources.CodeFragments.classes import IconConfig, ButtonConfig
from grand_battle.Resources.CodeFragments.other_functions import get_font, get_difficulty_description_parts
from grand_battle.Resources.CodeFragments.database_functions import get_data

Button_config = ButtonConfig()

data = get_data({})


def get_c_d(CHOSEN_DIFFICULTY):
    c_d = 0
    if CHOSEN_DIFFICULTY == 'medium':
        c_d = 1
    if CHOSEN_DIFFICULTY == 'hard':
        c_d = 2
    if CHOSEN_DIFFICULTY == 'insane':
        c_d = 3
    return c_d


def blit_level_icons(level_icons):
    Button_config.SCREEN.blit(level_icons[0], (250, 150))
    Button_config.SCREEN.blit(level_icons[1], (600, 150))
    Button_config.SCREEN.blit(level_icons[2], (950, 150))
    Button_config.SCREEN.blit(level_icons[3], (250, 500))
    Button_config.SCREEN.blit(level_icons[4], (600, 500))
    Button_config.SCREEN.blit(level_icons[5], (950, 500))


def get_time_and_status(c_d, l_b):
    index = 62 + c_d * 36 + l_b * 4
    status = data[c_d * 10 + l_b][0] + " stars"
    time = data[index][:2] + " hr " + data[index + 1][:2] + " min " + data[index + 2][:2] + " sec"
    if data[c_d * 10 + l_b][0] == '0':
        status = "not completed"
    if data[index][:2] == "00" and data[index + 1][:2] == "00" and data[index + 2][:2] == "00":
        time = "-"

    return time, status


class Button:
    def __init__(self, image, image_path, pos, difficulty_button=0, level_button=0, endless_button=0):
        self.image = image
        self.image_path = image_path
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.difficulty_button = difficulty_button
        self.level_button = level_button
        self.endless_button = endless_button

    def update(self, SCREEN):
        if self.image is not None:
            SCREEN.blit(self.image, self.rect)

    def checkForInput(self, position):
        return position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom)

    def changeCondition(self, position, CHOSEN_DIFFICULTY='beginner'):
        c_d = get_c_d(CHOSEN_DIFFICULTY)
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.image_path = self.image_path[:Button_config.PATH_INDENT] + "_enabled.png"
            self.image = pygame.image.load(self.image_path)
        else:
            self.image_path = self.image_path[:Button_config.PATH_INDENT] + "disabled.png"
            self.image = pygame.image.load(self.image_path)
        if self.endless_button:
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom):
                personal_best_text = get_font(Button_config.LEVEL_STATUS_FONT_SIZE).render(
                    "Personal best: " + data[len(data) - 1] + " metres",
                    True, "#b68f40")
                personal_best_rect = personal_best_text.get_rect(center=(1000, 900))
                Button_config.SCREEN.blit(personal_best_text, personal_best_rect)

        if self.level_button:
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom):
                l_b = self.level_button - 1
                time, status = get_time_and_status(c_d, l_b)
                level_status_text = get_font(Button_config.LEVEL_STATUS_FONT_SIZE).render("Status: " + status, True,
                                                                                          "#b68f40")
                level_status_rect = level_status_text.get_rect(center=(1000, 840))
                level_time_text = get_font(Button_config.LEVEL_STATUS_FONT_SIZE).render("Time: " + time, True,
                                                                                        "#b68f40")
                level_time_rect = level_time_text.get_rect(center=(1000, 870))
                Button_config.SCREEN.blit(level_status_text, level_status_rect)
                Button_config.SCREEN.blit(level_time_text, level_time_rect)
        if self.difficulty_button:
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom):
                stars_arr = []
                for i in range(9):
                    stars_arr.append(data[(self.difficulty_button - 1) * 10 + i][0])

                Icon_config = IconConfig()
                Icon_config.initialize_icon_paths(stars_arr)

                level_icons = Icon_config.initialize_icon_images()

                blit_level_icons(level_icons)

                difficulty_description = pygame.image.load("../Textures/difficulty_description_label.png")
                Button_config.SCREEN.blit(difficulty_description, (400, 500))
                get_difficulty_description_parts(self.difficulty_button, Button_config)
            else:
                self.image_path = self.image_path[:Button_config.PATH_INDENT] + "disabled.png"
                self.image = pygame.image.load(self.image_path)
