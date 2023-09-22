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
    pygame.display.set_caption('CSW Hangman game')
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
    count = 0
    hangman, word, hint = gallow()
    myTemplate = Template(word, hint)

    # Button variables
    letters = []
    radius = 15
    gap = 10
    A = 65
    x = int((surface.get_width() - (radius * 2 + gap) * 13) / 2)
    y = 400
    for i in range(26):
        letters.append([x, y, chr(A+i), True])
        x += radius * 2 + gap
        if i == 12:
            x = int((surface.get_width() - (radius * 2 + gap) * 13) / 2)
            y = 400 + radius * 2 + gap

    # Play the game until the player closes the window
    while opened:
        opened = control_game(letters, radius, myTemplate)
        if not myTemplate.is_complete():
            game_screen(surface, myTemplate, hangman, letters, radius)
        ##################################################
        # Challenge 1 and 2
        # Display game ending message, such as the correct word and whether they win
        # Flashing the messages between green, blue and black
        else:
            finished_screen(surface, myTemplate, count)
            count += 1
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
    alist = content.splitlines()

    # Choose a random entry
    entry = random.choice(alist)

    # Separate the word and the hint
    word, hint = entry.split(',')
    return [hangman, word.upper(), hint.upper()]


def control_game(letters, radius, myTemplate):
    # Update the template according to player's input
    opened = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            opened = False
        elif event.type == KEYDOWN and not myTemplate.is_complete():
            # Player enters words by keyboard
            if 97 <= event.key <= 97 + 26:
                myTemplate.update(chr(event.key).upper())
                letters[event.key-97][3] = False
        ##################################################
        # Challenge 3
        # Player can also choose correct words by pressing the button on the screen
        elif event.type == MOUSEBUTTONDOWN and not myTemplate.is_complete():
            # Player clicks on the letter on the screen
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                distance = sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)
                if distance < radius:
                    myTemplate.update(ltr)
                    letter[3] = False
        ##################################################
    return opened


def game_screen(surface, myTemplate, hangman, letters, radius):
    # Draw all game objects
    black = pygame.Color('black')
    white = pygame.Color('white')
    surface.fill(white)         # clear the display surface first

    # Fonts
    LETTER_FONT = pygame.font.SysFont('freesansbold.ttf', 30)
    WORD_FONT = pygame.font.SysFont('freesansbold.ttf', 60)
    TITLE_FONT = pygame.font.SysFont('freesansbold.ttf', 70)

    # Draw the title
    title = TITLE_FONT.render('CSW Hangman Game', True, black)
    surface.blit(title, ((surface.get_width()-title.get_width())//2, 20))

    # Draw the hangman
    surface.blit(hangman[myTemplate.status], (150, 100))

    # Draw the template
    dashes = WORD_FONT.render(' '.join(myTemplate.dashes), True, black)
    surface.blit(dashes, (320, 250))

    # Draw the hint
    hint = WORD_FONT.render(myTemplate.hint, True, black)
    surface.blit(hint, ((surface.get_width()-hint.get_width())//2, 320))

    # Draw buttons
    for letter in letters:
        if letter[3]:
            pygame.draw.circle(surface, black, (letter[0], letter[1]), radius, 3)
            text = LETTER_FONT.render(letter[2], True, black)
            surface.blit(text, (letter[0]-text.get_width()/2, letter[1]-text.get_height()/2))

    pygame.display.update()     # Update the display surface


##################################################
# Challenge 1 and 2
# Display game ending message, such as the correct word and whether they win
# Flashing the messages between green, blue and black
def finished_screen(surface, myTemplate, count):
    # Display game ending congratulation texts
    color = ['black', 'green', 'blue']
    if myTemplate.is_complete() == -1:
        text = 'Better luck next time!'
    else:
        text = 'Congratulation! You win!'

    surface.fill(pygame.Color('white'))
    font = pygame.font.Font('freesansbold.ttf', 45)
    correct = font.render('The correct word is '+myTemplate.word+'!', True, pygame.Color(color[(count//50) % 3]))
    string = font.render(text, True, pygame.Color(color[(count//50) % 3]))

    x = int(surface.get_width()/2 - correct.get_width()/2)
    y = int(surface.get_height()/2 - correct.get_height()/2)
    surface.blit(correct, (x, y))

    x = int(surface.get_width()/2 - string.get_width()/2)
    y += correct.get_height()
    surface.blit(string, (x, y))
    pygame.display.update()
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
        for i in range(len(self.word)):
            if self.word[i] == char:
                self.dashes[i] = char
                update = True
        if not update:
            self.status += 1
        return update

    def is_complete(self):
        # Check whether the game has completed
        # Returns -1 if the player has exceeds the max number of tries
        # Returns 0 if the game is not completed
        # Returns 1 if the player wins
        if self.status >= 6:
            return -1
        elif '_' in self.dashes:
            return 0
        else:
            return 1


if __name__ == '__main__':
    main()
