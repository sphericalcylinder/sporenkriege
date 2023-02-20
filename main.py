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
pygame.display.set_caption("Sporenkriege")
pygame.event.set_allowed([pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.KEYDOWN])

MAP = pygame.surface.Surface((128,128))

CLOCK = pygame.time.Clock()

closegame = False


enemy_group = pygame.sprite.Group()
tendril_group = pygame.sprite.Group()
node_group = pygame.sprite.Group()

def mainmenu(gamestate):

    play = Classes.Button(
        (SCREEN_WIDTH/2)-64, (SCREEN_HEIGHT/2)-64, 'assets/staststop2.png')

    while gamestate == 0:
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

def init_player():
    player_nubs = []
    spawn_blacklist = []
    player = Classes.Player
    player.x = 0
    player.y = 0
    spawn_blacklist.append(player)
    player_nubs.append(player)

def enemy_turn(game_iteration, spawn_blacklist: list):
    
    #Form new enemies
    enemy_randomness = settings['enemy_randomness']
    enemy_count = round((settings['slope'] * game_iteration + 1) * random.uniform(1-enemy_randomness, 1+enemy_randomness), None)

    invalid_x, invalid_y = set(point[0] for point in spawn_blacklist), set(point[1] for point in spawn_blacklist)
    valid_x, valid_y = (set(range(128)) - invalid_x), (set(range(128)) - invalid_y)
    spawn_x, spawn_y = random.choice(valid_x), random.choice(valid_y)
    enemy_group.add(Classes.Enemy(spawn_x, spawn_y, '#8B4513'))

    spawn_blacklist.append(*[(spawn_x-1, spawn_y-1),(spawn_x, spawn_y-1),(spawn_x+1, spawn_y-1) ,
                             (spawn_x-1,   spawn_y),(spawn_x,   spawn_y),(spawn_x+1,   spawn_y) ,
                             (spawn_x-1, spawn_y+1),(spawn_x, spawn_y+1),(spawn_x+1, spawn_y+1)])


def check_win_loss(player_nubs, gamestate):
    if player_nubs <= 0:
        return 2
    #Wubby note - decide on win states later (2/20/23)

def player_turn():
    pass

def game(gamestate):

    game_iteration = 0
    drawlist = []
    
    while gamestate == 1:
        #GAME LOGIQUE!!!!!
        
            
        # Clear screen
        SCREEN.fill((0, 0, 0))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    print('new hub')

        # Draw stuff
        

        for i in drawlist:
            SCREEN.blit(i)

        # Update the screen
        pygame.display.update()
        # Set fps
        CLOCK.tick(settings['fps'])
    

# Main function


def main():

    gamestate = 0  # 0: Main Menu  1: Game  2: Death Screen

    while not closegame:
        if gamestate == 0:
            gamestate = mainmenu(gamestate)
            continue
        if gamestate == 1:
            gamestate = game(gamestate)
            continue


# Run main if not a module
if __name__ == '__main__':
    main()
