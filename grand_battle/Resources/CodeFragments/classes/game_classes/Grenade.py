import pygame

clock = pygame.time.Clock()
G = 0.5
CHARACTER_SPEED = 5


class Grenade(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_scroll, direction, MAP_MATRIX):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Textures/grenade.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity_x = 20
        self.velocity_y = -10
        self.screen_scroll = screen_scroll
        self.MAP_MATRIX = MAP_MATRIX

        self.size = self.image.get_size()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.direction = 0
        if direction == 1:
            self.direction = -1
        else:
            self.direction = 1

        self.velocity_x *= self.direction

    def update(self, change, char, screen_scroll):
        self.screen_scroll = screen_scroll
        if change[0] == 0 and change[1] and not change[3]:
            self.rect.x += CHARACTER_SPEED
        if change[0] == 0 and change[2] and not change[3]:
            self.rect.x -= CHARACTER_SPEED
        if self.velocity_y > 12:
            self.velocity_y = 12
        self.velocity_y += G
        if self.velocity_x:
            self.velocity_x -= 0.5 * G * self.direction

        if abs(self.velocity_x) <= 1 and self.velocity_x and self.velocity_y:
            self.velocity_x = self.direction

        x_change = 0
        if self.velocity_x:
            x_change = self.direction * self.velocity_x
        y_change = self.velocity_y

        for x in range(len(self.MAP_MATRIX)):
            for y in range(len(self.MAP_MATRIX[x])):
                block = self.MAP_MATRIX[x][y]
                tile = pygame.Rect((240 + y * 50 + self.screen_scroll, x * 50), (50, 50))

                if block == 'P':
                    if tile.colliderect(self.rect.x + x_change, self.rect.y, self.width,
                                        self.height) or tile.colliderect(self.rect.x, self.rect.y + y_change,
                                                                         self.width,
                                                                         self.height):
                        self.explode_grenade()

        self.rect.x += x_change
        self.rect.y += y_change

    def explode_grenade(self):
        pass
