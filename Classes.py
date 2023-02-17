import pygame
import random


class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, filename) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.image = pygame.image.load(filename)
        self.w, self.h = self.image.get_width(), self.image.get_height()

    def isclicked(self, clickx, clicky) -> bool:
        if clickx > self.x and clickx < self.x+self.w and clicky > self.y and clicky < self.y+self.h:
            return True
        else:
            return False


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, filename) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.image = pygame.image.load(filename)
        self.w, self.h = self.image.get_width(), self.image.get_height()
        self.health = 1000000000000  # wow
        self.bias = (random.randint(x-20, x+20), random.randint(y-20, y+20))

    def grow():
        pass
