class GlobalConstAndVarConfig:
    def __init__(self):
        self.SCREEN_WIDTH = 1920
        self.SCREEN_HEIGHT = 1080
        self.PATH_INDENT = -12
        self.DESCRIPTION_FONT_SIZE = 10
        self.LEVEL_STATUS_FONT_SIZE = 24
        self.FPS = 60
        self.G = 0.5
        self.OOB = (10000, 10000)
        self.GLOBAL_X = -500
        self.CHARACTER_SPEED = 5
        self.TURRETS_DESTROYED = 0
        self.screen_scroll = 0
        self.levels_page = 1
        self.data = ['-' for i in range(207)]
        self.CHOSEN_DIFFICULTY = 'beginner'
        self.SONG_VOLUME = 0
        self.SOUNDS_VOLUME = 0
        self.keybinds = dict()
        self.keyactions = dict()
        self.first_launch = True
