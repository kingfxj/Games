# This is a one player hangman game. The player will be given a hint
# and then they can use keyboard or the buttons on the screen to guess the word.
# The player has 6 tries. The play wins when they have correctly guessed the word.
# Challenge 1: Display game ending message, such as the correct word and whether they win.
# Challenge 2: Flashing the messages between green, blue and black.
# Challenge 3: Player can also choose correct words by pressing the button on the screen

import pygame
import random
from math import sqrt
from pygame.locals import *


def main():
    # Initial all pygame modules
    pygame.init()
    # Create a pygame window
    pygame.display.set_mode((700, 500))
    # Set the title of the display window
    pygame.display.set_caption('CSW Hangman game Template')
    # Get the surface of the window
    surface = pygame.display.get_surface()
    # Play the main game
    play_game(surface)
    # Quit pygame and clean pygame window
    pygame.quit()


def play_game(surface):
    # Initialize variables
    # Surface is the display window object
    opened = True
    hangman, word, hint = gallow()
    myTemplate = Template(word, hint)

    # Button variables
    letters = []
    radius = 15

    # Play the game until the player closes the window
    while opened:
        opened = control_game(letters, radius, myTemplate)
        if not myTemplate.is_complete():
            game_screen(surface, myTemplate, hangman, letters, radius)
        ##################################################
        # Challenge 1 and 2
        # Display game ending message, such as the correct word and whether they win
        # Flashing the messages between green, blue and black
        ##################################################
        pygame.time.Clock().tick(120)   # run at most with 120 Frames Per Second


def gallow():
    # Load variables for the hangman
    hangman = []
    for i in range(7):
        hangman.append(pygame.image.load("hangman" + str(i) + ".png"))

    # wordshint.txt is a file that contains a list of word and hints
    infile = open('wordshint.txt', 'r')
    content = infile.read()
    infile.close()

    # Choose a random entry

    # Separate the word and the hint

    return [hangman]


def control_game(letters, radius, myTemplate):
    # Update the template according to player's input
    opened = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            opened = False
        ##################################################
        # Challenge 3
        # Player can also choose correct words by pressing the button on the screen
        ##################################################
    return opened


def game_screen(surface, myTemplate, hangman, letters, radius):
    # Draw all game objects
    white = pygame.Color('white')
    surface.fill(white)         # clear the display surface first

    # Fonts

    # Draw the title

    # Draw the hangman

    # Draw the template

    # Draw the hint

    # Draw buttons

    pygame.display.update()     # Update the display surface


##################################################
# Challenge 1 and 2
# Display game ending message, such as the correct word and whether they win
# Flashing the messages between green, blue and black
def finished_screen(surface, myTemplate, count):
    # Display game ending congratulation texts
    pass
##################################################


class Template:
    def __init__(self, word, hint):
        self.word = word
        self.hint = hint
        self.dashes = ['_'] * len(word)
        self.status = 0

    def update(self, char):
        # update the template - if the template is updated the method return True otherwise it returns False
        # - self is the Template object
        # - word is the string that the user is trying to guess
        # - char is a string - it is the letter that the player has entered
        update = False
        return update

    def is_complete(self):
        # Check whether the game has completed
        # Returns -1 if the player has exceeds the max number of tries
        # Returns 0 if the game is not completed
        # Returns 1 if the player wins
        return -1


if __name__ == '__main__':
    main()
