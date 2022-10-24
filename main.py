import pygame
import sys
from settings import Settings
from ship import Ship

class AlienInvasion():

    def __init__(self):

        # initialize the game and create a screen object
        pygame.init()
        # create an object for the class Settings
        self.ai_settings = Settings()
        # create an object to configure screen
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        pygame.display.set_caption('Alien Invasion')


        # make a ship
        self.ship = Ship(self.screen)

    def run_game(self):
        while True:

            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # draw the screen
            self.screen.fill(self.ai_settings.bg_color)

            # Draw the ship at the location
            self.ship.blitme()
            # screen.blit(image, rect)

            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
