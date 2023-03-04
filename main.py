import sys
import pygame
import json
import Classes
import math
import random
import time

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
pygame.event.set_allowed(
    [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.KEYDOWN, pygame.KEYUP])

MAP = pygame.surface.Surface((512, 512))

CLOCK = pygame.time.Clock()

closegame = False

FUNGUSCOLOUR = '#8B4513'
enemy_group = []
tendril_group = []
node_group = []
hub_group = []
construction_ghost = []

spawn_blacklist = [(0, 0)]

keys = {
    pygame.K_g: False,
    pygame.K_a: False
}

keypressed = False
mousedown = False


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
        


def check_win_loss(player_nubs, gamestate):
    if player_nubs <= 0:
        return 2
    # Wubby note - decide on win states later (2/20/23)


def player_turn(mouse_button_up, ghosted_hub):
    if keys[pygame.K_g] and ghosted_hub == None:
        #Q: How do I add an object? A: MAGIC
        ghosted_hub = Classes.Hub(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], '#8B4513', False)
        construction_ghost.append(ghosted_hub)

def draw():
    for hub in hub_group:
        hub.draw(MAP)
    for node in node_group:
        node.draw(MAP)
    for tendril in tendril_group:
        tendril.draw(MAP)
    for ghost in construction_ghost:
        ghost.draw(MAP)
    for enemy in enemy_group:
        enemy.draw(MAP)

    SCREEN.blit(MAP, (0, 0))
    # Update the screen
    pygame.display.update()
    # Set fps
    CLOCK.tick(settings['fps'])

# Wubby note - LIFE PRO TIP - if you can't figure something out, and you know you've done it before, stop being an idiot. (2/23/23)


def events():
    global mousedown, keypressed, keys
    # Handle events
    keypressed = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            try:
                keys[event.key] = True
            except KeyError:
                pass
            keypressed = True

        if event.type == pygame.KEYUP:
            try:
                keys[event.key] = False
            except KeyError:
                pass
            keypressed = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True

        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False

def enemy_turn(game_iteration, timer):
    global spawn_blacklist
    
    # Form new enemies
    enemy_randomness = float(settings['enemy_randomness'])
    enemy_count = round((float(settings['slope']) * game_iteration + 1) *
                        random.uniform(1-enemy_randomness, 1+enemy_randomness), None)
    enemy_timer = Classes.Timer(timer.WAIT/enemy_count)
    for i in range(enemy_count):
        invalid_x, invalid_y = set(point[0] for point in spawn_blacklist), set(
            point[1] for point in spawn_blacklist)
        valid_x, valid_y = (
            set(range(MAP.get_width())).difference(invalid_x)), (set(range(MAP.get_height())).difference(invalid_y))
        spawn_x, spawn_y = random.choice(list(valid_x)), random.choice(list(valid_y))
        enemy_group.append(Classes.Enemy(spawn_x, spawn_y, '#8B4513'))

        spawn_blacklist.append((spawn_x-1, spawn_y-1))
        spawn_blacklist.append((spawn_x,   spawn_y-1))
        spawn_blacklist.append((spawn_x+1, spawn_y-1))
        spawn_blacklist.append((spawn_x-1, spawn_y  ))
        spawn_blacklist.append((spawn_x,   spawn_y  ))
        spawn_blacklist.append((spawn_x+1, spawn_y  ))
        spawn_blacklist.append((spawn_x-1, spawn_y+1))
        spawn_blacklist.append((spawn_x,   spawn_y+1))
        spawn_blacklist.append((spawn_x+1, spawn_y+1))
        enemy_timer.start()
        while not enemy_timer.isdone():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)

            draw()

def game(gamestate):

    game_iteration = 0
    timer = Classes.Timer(5)
    timer.start()

    while gamestate == 1:
        # GAME LOGIQUE!!!!!

        # Clear screen
        SCREEN.fill((0, 0, 0))

        events()
        ghosted_hub = None
        

        if not timer.isdone() and game_iteration % 2 == 0:
            player_turn(not mousedown, ghosted_hub)
        elif timer.isdone():
            game_iteration += 1
            ghosted_hub = None
            timer.start()

        if not timer.isdone() and game_iteration % 2 == 1:
            enemy_turn(game_iteration, timer)
        elif timer.isdone():
            game_iteration += 1
            ghosted_hub = None
            timer.start()

        # Draw stuff
        draw()

    return None


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
