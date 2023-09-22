# This is a two player Pong game. There are two rackets and one ball in the middle.
# Player 1 controls the left rackets by q (move the racket up) and a (move the racket down)
# Player 2 controls the right rackets by p (move the racket up) and l (move the racket down)
# If the ball hits the right edge of the window, the upper-left score will be added one.
# If the ball hits the left edge of the window, the upper-right score will be added one.
# The game ends when one player's score reach 11 and that player wins.
# Remove '#' to play against the computer. Computer controls the racket on the left side
# and player controls the racket on the right side using "p" and "l".
# Challenge 1: randomize the initial y position of the ball
# Challenge 2: Display which player wins at the end of the game
# Challenge 3: Flashing winning messages between green, blue and white
# Challenge 4: Make an AI racket

import pygame
import random
from pygame.locals import *


# User-defined functions
def main():
    # Initial all pygame modules
    pygame.init()
    # Create a pygame window
    pygame.display.set_mode((600, 500))
    # Set the title of the display window
    pygame.display.set_caption('CSW Pong game')
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
    winner = 0
    backgroundColor = pygame.Color('black')
    wordColor = pygame.Color('white')

    # Game specific variables
    score = [0, 0]
    rackets = [pygame.Rect(100, 200, 10, 100), pygame.Rect(500, 200, 10, 100)]
    movement = 10
    x = int(surface.get_width()/2)
    # y = int(surface.get_height()/2)
    # ##################################################
    # Challenge 1
    # Randomize initial y position
    y = random.randint(10, surface.get_height()-10)
    ##################################################
    ball = Ball(surface, wordColor, [x, y], [3, 6], 10, score)
    pygame.key.set_repeat(30, 30)
    count = 0

    # Play the game until the player closes the window.
    while opened:   # until player clicks close box
        opened = control_game(surface, movement, rackets, opened, winner)
        if not winner:
            # Update game objects
            ball.move(rackets)
            ball.change_direction()
            ##################################################
            # Challenge 4
            # Make an AI racket
            # computer(surface, movement*3//2, rackets, ball)
            ##################################################
            game_screen(surface, backgroundColor, score, wordColor, rackets, ball)
        winner = is_game_finished(score)
        ##################################################
        # Challenge 2 and 3
        # Display which player wins at the end of the game
        # Flashing winning messages between green, blue and white
        if winner != 0:
            # Show winning message
            finished_screen(surface, backgroundColor, winner, count)
            count += 1
        ##################################################
        pygame.time.Clock().tick(120)   # run at most with 120 Frames Per Second


def control_game(surface, movement, rackets, opened, winner):
    # Control the movement of the paddle according to player's input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            opened = False
        elif event.type == KEYDOWN:
            if not winner:
                keys = pygame.key.get_pressed()             # Record the keys that are pressed
                if keys[K_q] and rackets[0].top >= 0:
                    # The left paddle is in the window
                    rackets[0].move_ip(0, -movement)        # Move the paddle up
                if keys[K_a] and rackets[0].bottom <= surface.get_height():
                    # The left paddle is in the window
                    rackets[0].move_ip(0, movement)         # Move the paddle down
                if keys[K_p] and rackets[1].top >= 0:
                    # The right paddle is in the window
                    rackets[1].move_ip(0, -movement)        # Move the paddle up
                if keys[K_l] and rackets[1].bottom <= surface.get_height():
                    # The right paddle is in the window
                    rackets[1].move_ip(0, movement)         # Move the paddle down
    return opened


##################################################
# Challenge 4
# Make an AI racket
def computer(surface, movement, rackets, ball):
    # Computer controls the paddle on the left according to the position of the balls
    if rackets[0].bottom > ball.center[1] and rackets[0].top >= 0:
        rackets[0].move_ip(0, -movement)
    elif rackets[0].bottom < ball.center[1] and rackets[0].bottom < surface.get_height():
        rackets[0].move_ip(0, movement)
##################################################


def game_screen(surface, backgroundColor, score, wordColor, rackets, ball):
    # Draw all game objects.
    surface.fill(backgroundColor)           # clear the display surface first
    font = pygame.font.Font('freesansbold.ttf', 72)
    leftScore = font.render(str(score[0]), False, wordColor)
    rightScore = font.render(str(score[1]), False, wordColor)
    surface.blit(leftScore, (0, 0))
    surface.blit(rightScore, (surface.get_width()-rightScore.get_width(), 0))
    for racket in rackets:
        pygame.draw.rect(surface, wordColor, racket)
    ball.display()
    pygame.display.update()                 # Update the display surface


def is_game_finished(score):
    # Check and remember if the game is finished
    # Return the winner, 1 means the player 1 wins and 2 means player 2 wins
    # Return 0 if the game is not finished
    if score[0] >= 11:
        return 1
    elif score[1] >= 11:
        return 2
    else:
        return 0


##################################################
# Challenge 2 and 3
# Display which player wins at the end of the game
# Flashing winning messages between green, blue and white
def finished_screen(surface, backgroundColor, winner, count):
    # Display game ending congratulation texts
    color = ['white', 'green', 'blue']
    text = 'Congratulation, '
    if winner == 1:
        text += 'left player wins!'
    else:
        text += 'right player wins!'
    surface.fill(backgroundColor)
    font = pygame.font.Font('freesansbold.ttf', 45)
    string = font.render(text, False, pygame.Color(color[(count//50) % 3]))
    x = int(surface.get_width()/2 - string.get_width()/2)
    y = int(surface.get_height()/2 - string.get_height()/2)
    surface.blit(string, (x, y))
    pygame.display.update()
##################################################


class Ball:
    # An object in this class represents a Ball that moves
    def __init__(self, surface, color, center, velocity, radius, score):
        # Initialize a Ball.
        # - self is the Ball to initialize
        # - surface is the window's pygame.Surface object
        # - color is the pygame.Color of the dot
        # - center is a list containing the x and y int coords of the center of the ball
        # - velocity is a list containing the x and y components
        # - radius is the int pixel radius of the dot
        # - score is the list of the two players' score
        self.surface = surface
        self.color = color
        self.center = center
        self.velocity = velocity
        self.radius = radius
        self.score = score

    def move(self, rackets):
        # Change the location of the Ball by adding the corresponding
        # speed values to the x and y coordinate of its center
        # - self is the Ball
        size = self.surface.get_size()
        for coordinate in range(2):
            self.center[coordinate] += self.velocity[coordinate]
            if self.center[coordinate] < self.radius or self.center[coordinate] + self.radius > size[coordinate]:
                self.velocity[coordinate] = -self.velocity[coordinate]

        # The ball will bounce off the front of the racket but go through the back of the racker
        for coordinate in range(2):
            if rackets[coordinate].collidepoint(self.center):
                self.velocity[0] = (-1)**coordinate * abs(self.velocity[0])

    def change_direction(self):
        # Change the direction of the ball if it bounces off the wall or the rackets
        if self.center[0] < self.radius:
            self.score[1] += 1
        elif self.center[0] + self.radius > self.surface.get_width():
            self.score[0] += 1

    def display(self):
        # Display the ball on the surface
        # - self is the Ball
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)


if __name__ == "__main__":
    main()
