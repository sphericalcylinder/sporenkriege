import sys
import pygame
import json

# Initialize pygame
pygame.init()
#pygame.font.init()

# Set up drawing area/screen and define constants
SCREEN = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Sporenkriege")
pygame.event.set_allowed(None)

CLOCK = pygame.time.Clock()

# Get python dict from settings.json file
def parse_settings():
    with open('settings.json', 'r') as f:
        return json.load(f)

# Main function
def main():

    settings = parse_settings()

    while True:
        # Clear screen
        SCREEN.fill(settings['bg'])

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

        # Draw stuff
        # ...

        # Update the screen
        pygame.display.update()
        # Set fps
        CLOCK.tick(settings['fps'])


# Run main if not a module
if __name__ == '__main__':
    main()
