import pygame

from Resources.CodeFragments.level_functions import level_launch, endless_mode
from Resources.CodeFragments.menu_functions import keybinding, main_menu
from Resources.CodeFragments.menu_functions import options_audio, options_keyboard, options_video
from Resources.CodeFragments.menu_functions.other_menu.play import play


class Menu:
    def __init__(self, SCREEN, CANVAS, CAV_config, MUSIC_config, IMAGES_config, MAPS_config, GROUPS_config):
        self.SCREEN = SCREEN
        self.CANVAS = CANVAS
        self.CAV_config = CAV_config
        self.MUSIC_config = MUSIC_config
        self.IMAGES_config = IMAGES_config
        self.MAPS_config = MAPS_config
        self.GROUPS_config = GROUPS_config
        self.clock = pygame.time.Clock()

    def choose_transition(self, transition_info):
        if transition_info[0] == 'main_menu':
            self.main_menu_transition()
        if transition_info[0] == 'options_audio':
            self.options_audio_transition()
        if transition_info[0] == 'options_video':
            self.options_video_transition()
        if transition_info[0] == 'options_keyboard':
            self.options_keyboard_transition()
        if transition_info[0] == 'keybinding':
            self.keybinding_transition(self.clock)
        if transition_info[0] == 'play':
            self.play_transition()
        if transition_info[0] == 'level_launch':
            self.level_launch_transition(transition_info[1], self.clock)
        if transition_info[0] == 'endless_mode':
            self.endless_mode_transition(self.clock)

    def main_menu_transition(self):
        returned_list = main_menu(self.SCREEN, self.CANVAS, self.CAV_config, self.MUSIC_config, self.IMAGES_config,
                                  self.MAPS_config, self.GROUPS_config)
        self.choose_transition(returned_list[:3])

    def options_audio_transition(self):
        returned_list = options_audio(self.SCREEN, self.CANVAS, self.CAV_config, self.MUSIC_config, self.IMAGES_config,
                                      self.MAPS_config, self.GROUPS_config)
        self.choose_transition(returned_list[:3])

    def options_video_transition(self):
        returned_list = options_video(self.SCREEN, self.CANVAS, self.CAV_config, self.MUSIC_config, self.IMAGES_config,
                                      self.MAPS_config, self.GROUPS_config)
        self.choose_transition(returned_list[:3])

    def options_keyboard_transition(self):
        returned_list = options_keyboard(self.SCREEN, self.CANVAS, self.CAV_config, self.MUSIC_config,
                                         self.IMAGES_config, self.MAPS_config, self.GROUPS_config)
        self.choose_transition(returned_list[:3])

    def keybinding_transition(self, action):
        returned_list = keybinding(action, self.SCREEN, self.CANVAS, self.CAV_config, self.MUSIC_config,
                                   self.IMAGES_config, self.MAPS_config, self.GROUPS_config)
        self.choose_transition(returned_list[:3])

    def play_transition(self):
        returned_list = play(self.SCREEN, self.CANVAS, self.CAV_config, self.MUSIC_config, self.IMAGES_config,
                             self.MAPS_config, self.GROUPS_config)
        self.choose_transition(returned_list[:3])

    def level_launch_transition(self, level_num, clock):
        returned_list = level_launch(level_num, clock, self.SCREEN, self.CANVAS, self.CAV_config, self.MUSIC_config,
                                     self.IMAGES_config, self.MAPS_config, self.GROUPS_config)
        self.choose_transition(returned_list[:3])

    def endless_mode_transition(self, clock):
        returned_list = endless_mode(clock, self.SCREEN, self.CANVAS, self.CAV_config, self.MUSIC_config,
                                     self.IMAGES_config,
                                     self.MAPS_config, self.GROUPS_config)
        self.choose_transition(returned_list[:3])
