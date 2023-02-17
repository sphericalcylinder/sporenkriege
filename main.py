import sys
import pygame
import json
import Classes

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
pygame.display.set_caption("Sporenkriege")
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])

CLOCK = pygame.time.Clock()

closegame = False


def mainmenu(playstate):

    play = Classes.Button(
        (SCREEN_WIDTH/2)-64, (SCREEN_HEIGHT/2)-64, 'assets/staststop2.png')

    while playstate == 0:
        SCREEN.fill(settings['bg'])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.isclicked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
                    return 1

        # Draw stuff
        SCREEN.blit(play.image, (play.x, play.y))

        # Update the screen
        pygame.display.update()
        # Set fps
        CLOCK.tick(settings['fps'])


def game(playstate):

    drawlist = []

    while playstate == 1:

        # Clear screen
        SCREEN.fill((0, 0, 0))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        # Draw stuff
        

        for i in drawlist:
            SCREEN.blit(i)

        # Update the screen
        pygame.display.update()
        # Set fps
        CLOCK.tick(settings['fps'])

# Main function


def main():

    playstate = 0  # 0: Main Menu  1: Game  2: Death Screen

    while not closegame:
        print(playstate)
        if playstate == 0:
            playstate = mainmenu(playstate)
            continue
        if playstate == 1:
            playstate = game(playstate)
            continue


# Run main if not a module
if __name__ == '__main__':
    main()
 # What's so funny about Sussus Amogus?
