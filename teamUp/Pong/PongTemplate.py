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


# User-defined functions
def main():
    # Initial all pygame modules
    pygame.init()
    # Create a pygame window
    pygame.display.set_mode((600, 500))
    # Set the title of the display window
    pygame.display.set_caption('CSW Pong game Template')
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
    score = []

    ##################################################
    # Challenge 1
    # Randomize initial y position of the ball
    ##################################################

    ball = Ball(surface, wordColor, [300, 250], [3, 6], 10, score)
    pygame.key.set_repeat(30, 30)

    # Play the game until the player closes the window.
    while opened:   # until player clicks close box
        opened = control_game(opened)
        if not winner:
            # Update game objects
            ball.move()

            ##################################################
            # Challenge 4
            # Make an AI racket
            ##################################################

            game_screen(surface, backgroundColor, ball)
        winner = is_game_finished()

        ##################################################
        # Challenge 2 and 3
        # Display which player wins at the end of the game
        # Flashing winning messages between green, blue and white
        ##################################################

        pygame.time.Clock().tick(120)   # run at most with 120 Frames Per Second


def control_game(opened):
    # Control the movement of the paddle according to player's input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            opened = False
    return opened


##################################################
# Challenge 4
# Make an AI racket
def computer():
    # Computer controls the paddle on the left according to the position of the balls
    pass
##################################################


def game_screen(surface, backgroundColor, ball):
    # Draw all game objects.
    surface.fill(backgroundColor)           # clear the display surface first
    ball.display()
    pygame.display.update()                 # Update the display surface


def is_game_finished():
    # Check and remember if the game is finished
    # Return the winner, 1 means the player 1 wins and 2 means player 2 wins
    # Return 0 if the game is not finished
    return False


##################################################
# Challenge 2 and 3
# Display which player wins at the end of the game
# Flashing winning messages between green, blue and white
def finished_screen(surface, backgroundColor):
    # Display game ending congratulation texts
    surface.fill(backgroundColor)
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

    def move(self):
        # Change the location of the Ball by adding the corresponding
        # speed values to the x and y coordinate of its center
        # - self is the Ball
        for coordinate in range(2):
            self.center[coordinate] += self.velocity[coordinate]

    def display(self):
        # Display the ball on the surface
        # - self is the Ball
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)


if __name__ == "__main__":
    main()
