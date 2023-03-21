import pygame
import random
import time

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

class Timer():

    def __init__(self, delay) -> None:
        self.WAIT = delay
        self.timer = time.time()
    
    def start(self):
        self.timer = time.time() + self.WAIT

    def isdone(self) -> bool:
        if time.time() > self.timer:
            return True
        else:
            return False


class Node(pygame.sprite.Sprite):

    def __init__(self, x, y, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.w, self.h = 0, 0
        self.color = color
        self.rect = None

    def draw(self, map):
        self.rect = pygame.draw.circle(map, self.color, (self.x, self.y), 5.0)
        self.w, self.h = self.rect.w, self.rect.h

    def isclicked(self, clickx, clicky) -> bool:
        if clickx > self.x and clickx < self.x+self.w and clicky > self.y and clicky < self.y+self.h:
            return True
        else:
            return False


class Tendril(pygame.sprite.Sprite):

    def __init__(self, coord1, coord2, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x1, self.y1, self.x2, self.y2 = coord1[0], coord1[1], coord2[0], coord2[1]
        self.color = color

    def draw(self, map):
        pygame.draw.line(map, self.color, (self.x1, self.y1),
                         (self.x2, self.y2))


class Hub(pygame.sprite.Sprite):

    def __init__(self, x, y, color, ghost) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.color = color
        self.ghost = ghost

    def draw(self, map: pygame.surface.Surface):
        if self.ghost:
            transparent = pygame.surface.Surface((20, 20), pygame.SRCALPHA)
            pygame.draw.circle(transparent, self.color, (10, 10), 10.0)
            map.blit(transparent, (self.x-10, self.y-10))
        else:
            pygame.draw.circle(map, self.color, (self.x, self.y), 10.0)



class Fungus(pygame.sprite.Sprite):

    def __init__(self, x, y, color) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x, self.y = x, y
        self.health = 100
        self.bias = [0, 0]
        self.switch = 0
        self.network = [Hub(self.x, self.y, color, False)]

    def grow(self):
        if self.x == self.bias[0] and self.y == self.bias[1]:
            if type(self.bias) == tuple:
                self.bias = (random.randint(self.x-20, self.x+20),
                             random.randint(self.y-20, self.y+20))

        if self.switch == 0:
            self.network.append(Tendril(0, 0, None))
            self.switch = 1
        if self.switch == 1:
            self.network.append(Node(0, 0, None))
            self.switch = 0

    def draw(self, map):
        for i in self.network:
            i.draw(map)


class Player(Fungus):

    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color)
        self.bias = []


class Enemy(Fungus):

    def __init__(self, x, y, color) -> None:
        super().__init__(x, y, color)
        self.bias = (random.randint(self.x-10, self.x+10),
                     random.randint(self.y-10, self.y+10))
