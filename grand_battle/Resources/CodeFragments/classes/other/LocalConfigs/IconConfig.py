import pygame


class IconConfig:
    def __init__(self):
        self.icon_paths = []
        self.icon_images = []

    def initialize_icon_paths(self, stars_arr):
        for i in range(6):
            current_icon_path = f"../Textures/Level buttons/level0{i + 1}_button_stars-{stars_arr[i][0]}_disabled.png"
            self.icon_paths.append(current_icon_path)

    def initialize_icon_images(self):
        for i in range(6):
            self.icon_images.append(pygame.image.load(self.icon_paths[i]))

        return self.icon_images

