import pygame

from grand_battle.Resources.CodeFragments.classes import TurretConfig
from .EnemyBullet import EnemyBullet

Turret_config = TurretConfig()


class Turret(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, health, bullet_speed, MAP_MATRIX, CHOSEN_DIFFICULTY, CAV_config):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Textures/turret.png')
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.x = pos_x
        self.y = pos_y
        self.size = self.image.get_size()
        self.health = health
        self.look_direction = -1
        self.change_direction = False
        self.cooldown = 60 - CHOSEN_DIFFICULTY * 5
        self.CHOSEN_DIFFICULTY = CHOSEN_DIFFICULTY
        self.bullet_speed = bullet_speed
        self.MAP_MATRIX = MAP_MATRIX
        self.CAV_config = CAV_config

    def shoot(self):
        if self.look_direction == 1:
            return EnemyBullet(self.rect.x + self.size[0], self.rect.y + self.size[1] // 3 + 9,
                               self.bullet_speed, self.look_direction, self.MAP_MATRIX)
        return EnemyBullet(self.rect.x, self.rect.y + self.size[1] // 3 + 9, self.bullet_speed,
                           self.look_direction, self.MAP_MATRIX)

    def update(self, change, char):
        if change[0] == 0 and change[1] and not change[3]:
            self.rect.x += Turret_config.CHARACTER_SPEED
        if change[0] == 0 and change[2] and not change[3]:
            self.rect.x -= Turret_config.CHARACTER_SPEED

        if (char.rect.right + 20 < self.rect.left) and abs(self.rect.bottom - char.rect.bottom) < 50:
            self.look_direction = -1
            self.change_direction = False
        if (char.rect.left - 20 > self.rect.right) and abs(self.rect.bottom - char.rect.bottom) < 50:
            self.look_direction = 1
            self.change_direction = True

        Turret_config.SCREEN.blit(pygame.transform.flip(self.image, self.change_direction, False), self.rect)

        if self.health < 1:
            destruction_sound = pygame.mixer.Sound("Sounds/destruction_sound.mp3")
            destruction_sound.play()
            destruction_sound.set_volume(self.CAV_config.SOUNDS_VOLUME / 100)
            Turret_config.TURRETS_DESTROYED += 1
            self.kill()
            return [self.rect.x, self.rect.y]

        if 0 < self.rect.left - char.rect.right < 700 and abs(self.rect.bottom - char.rect.bottom) < 50:
            if self.cooldown > 0:
                self.cooldown -= 1
            if self.cooldown == 0:
                self.cooldown = 60 - self.CHOSEN_DIFFICULTY * 5
                if self.look_direction == 1:
                    return [str(self.rect.x + self.size[0]), str(self.rect.y + self.size[1] // 3 + 9),
                            str(self.bullet_speed), str(self.look_direction)]
                else:
                    return [str(self.rect.x), str(self.rect.y + self.size[1] // 3 + 9),
                            str(self.bullet_speed), str(self.look_direction)]

        if 0 < char.rect.left - self.rect.right < 700 and abs(self.rect.bottom - char.rect.bottom) < 50:
            if self.cooldown > 0:
                self.cooldown -= 1
            if self.cooldown == 0:
                self.cooldown = 60 - self.CHOSEN_DIFFICULTY * 5
                if self.look_direction == 1:
                    return [str(self.rect.x + self.size[0]), str(self.rect.y + self.size[1] // 3 + 9),
                            str(self.bullet_speed), str(self.look_direction)]
                else:
                    return [str(self.rect.x), str(self.rect.y + self.size[1] // 3 + 9),
                            str(self.bullet_speed), str(self.look_direction)]
