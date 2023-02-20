import sys
import pygame
import json
import Classes
import math, random

# Initialize pygame
pygame.init()
# pygame.font.init()

# Get python dict from settings.json file
def parse_settings():
    with open('settings.json', 'r') as f:
        return json.load(f)


settings = parse_settings()

SCREEN_WIDTH = settings['resolution'][0]
SCREEN_HEIGHT = settings['resolution'][1]

# Set up drawing area/screen and define constants
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sporenkriege Test")
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])

MAP = pygame.surface.Surface((128,128))

CLOCK = pygame.time.Clock()


node = Classes.Node(10, 10, '#8B4513')
tendril = Classes.Tendril((10, 10), (50, 50), '#8B4513')


while True:

    SCREEN.fill((0, 0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    #MAP = pygame.transform.scale(MAP, (128, 128))
    node.draw(MAP)
    tendril.draw(MAP)
    #MAP = pygame.transform.scale(MAP, (256, 256))
    SCREEN.blit(MAP, (0,0))

    # Update the screen
    pygame.display.update()
    # Set fps
    CLOCK.tick(settings['fps'])