import pygame
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy1.png")
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),
                                         randint(-5 * self.rect.height, -5))
        self.speed =2
        self.mask = pygame.mask.from_surface(self.image)
        self.active = True

        self.destroy_images = [pygame.image.load("image/enemy1_down1.png"),
                               pygame.image.load("image/enemy1_down2.png"),
                               pygame.image.load("image/enemy1_down3.png"),
                               pygame.image.load("image/enemy1_down4.png")]

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),
                                         randint(-5 * self.rect.height, 0))
        self.active = True

class MidEnemy(pygame.sprite.Sprite):
    energy = 5
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy2.png")
        self.image_hit = pygame.image.load("image/enemy2_hit.png")
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),
                                         randint(-10 * self.rect.height, -self.rect.height))
        self.speed = 1
        self.mask = pygame.mask.from_surface(self.image)
        self.active = True
        self.hit = False

        self.destroy_images = [pygame.image.load("image/enemy2_down1.png"),
                               pygame.image.load("image/enemy2_down2.png"),
                               pygame.image.load("image/enemy2_down3.png"),
                               pygame.image.load("image/enemy2_down4.png")]
        self.energy = MidEnemy.energy

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),
                                         randint(-10 * self.rect.height, -self.rect.height))
        self.active = True
        self.hit = False

        self.energy = MidEnemy.energy

class BigEnemy(pygame.sprite.Sprite):
    energy = 15
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("image/enemy3_n1.png")
        self.image2 = pygame.image.load("image/enemy3_n2.png")
        self.image_hit = pygame.image.load("image/enemy3_hit.png")
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),
                                         randint(-15 * self.rect.height, -5 * self.rect.height))
        self.speed = 2
        self.mask = pygame.mask.from_surface(self.image1)
        self.active = True
        self.hit = False

        self.destroy_images = [pygame.image.load("image/enemy3_down1.png"),
                               pygame.image.load("image/enemy3_down2.png"),
                               pygame.image.load("image/enemy3_down3.png"),
                               pygame.image.load("image/enemy3_down4.png"),
                               pygame.image.load("image/enemy3_down5.png"),
                               pygame.image.load("image/enemy3_down6.png")]
        self.energy = BigEnemy.energy

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),
                                         randint(-15 * self.rect.height, -5 * self.rect.height))
        self.active = True
        self.hit = False
        self.energy = BigEnemy.energy