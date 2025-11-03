import pygame
from random import randint
from util_params import *


class BlowFish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.vx = randint(-4,-1)
        self.vy = randint(-2,2)
        self.x = WIDTH + 100
        self.y = randint(0, HEIGHT)
        self.image = pygame.image.load('assets/images/fish_brown.png')
        self.image =  pygame.transform.flip(self.image, 1, 0)
        self.image = pygame.transform.rotozoom(self.image, 0, 1)
        self.rect = self.image.get_rect()

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.center = (self.x, self.y)
    

    def draw(self, screen):
        screen.blit(self.image, self.rect)

