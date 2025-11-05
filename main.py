'''This is the main code for the game'''
import pygame
import time
import random
import sys
from button import Button
from sprites import *
from config import *
pygame.font.init() # Initialize font module

class Game:
    '''Main game object which initializes the window and calls the main functions'''
    def __init__(self):
        pygame.init() # Initialize pygame library
        pygame.display.set_caption("Bacteria Conquest") # Set screen name
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT)) # Initialize the screen
        self.clock = pygame.time.Clock() # Initialize the clock
        #self.font = pygame.font.Font('cambria', 15) # Initialize font for writing
        self.running = True # Used to stop the game

    def createTilemap(self):
        '''Function for map logic'''
        # Looking at the tilemap, i = y co-ordinate
        for i, row in enumerate(tilemap):
            # j = x co-ordinate
            for j, column in enumerate(row):
                # If tilemap say B, spawn block sprite
                if column == "B":
                    Block(self, j, i)
                # If tilemap say E, spawn an enemy sprite
                if column == "E":
                    Enemy(self, j, i)
                # If tilemap say P, spawn player sprite
                if column == "P":
                    self.player = Player(self, j, i)
                    

    def new(self):
        '''Sets up the variables for a new game'''
        self.playing = True # Set the game to playing

        # Set the layers
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.player = None # ensure player attribute exists before creating tilemap

        self.createTilemap() # Call the tilemap function

    def events(self):
        '''This function handles events e.g. key presses'''
        # This for loop will capture all events
        for event in pygame.event.get():
            # Handle pressing the close button
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        '''This function updates the screen 
        e.g. making sure game is not an image'''
        self.all_sprites.update() # Update all sprites
    
    def draw(self):
        '''Draws everything on the screen'''
        self.screen.fill((0, 0, 0)) # Fill the screen with black
        self.all_sprites.draw(self.screen) # Draws all the sprites on the screen
        self.clock.tick(FPS) # Limit the frame rate
        pygame.display.update() # Update the screen

    def main(self):
        '''Main function containing the game loop'''
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass

# This builds the game structure
g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()
pygame.quit()
sys.exit()