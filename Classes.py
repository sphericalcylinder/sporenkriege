import pygame
import random
from numpy import sort


class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.image = pygame.image.load(color)
        self.w, self.h = self.image.get_width(), self.image.get_height()

    def isclicked(self, clickx, clicky) -> bool:
        if clickx > self.x and clickx < self.x+self.w and clicky > self.y and clicky < self.y+self.h:
            return True
        else:
            return False



class Node(pygame.sprite.Sprite):
    
    def __init__(self, x, y, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.color = color

    def draw(self, map):
        pygame.draw.circle(map, self.color, (self.x, self.y), 5.0)

class Tendril(pygame.sprite.Sprite):
    
    def __init__(self, coord1, coord2, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x1, self.y1, self.x2, self.y2 = coord1[0], coord1[1], coord2[0], coord2[1]
        self.color = color

    def draw(self, map):
        pygame.draw.line(map, self.color, (self.x1, self.y1), (self.x2, self.y2))


class Hub(pygame.sprite.Sprite):
    
     def __init__(self, x, y, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.image = pygame.image.load(color)
        self.w, self.h = self.image.get_width(), self.image.get_height()


class Fungus(pygame.sprite.Sprite):

    def __init__(self, x, y, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.image = pygame.image.load(color)
        self.w, self.h = self.image.get_width(), self.image.get_height()
        self.health = 100
        self.bias = [0, 0]
        self.switch = 0
        self.network = []

    def grow(self):
        if self.x == self.bias[0] and self.y == self.bias[1]:
            if type(self.bias) == tuple:
                self.bias = (random.randint(self.x-20, self.x+20), random.randint(self.y-20, self.y+20))
        
        if self.switch == 0:
            self.network.append(Tendril(0,0,None))
            self.switch = 1
        if self.switch == 1:
            self.network.append(Node(0,0,None))
            self.switch = 0

        


class Player(Fungus):

    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color)
        self.bias = []

class Enemy(Fungus):

    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color)
        self.bias = (random.randint(self.x-10, self.x+10), random.randint(self.y-10, self.y+10))
