import pygame
import random
from pygame.locals import *

# Initial all pygame modules
pygame.init()
# Create a pygame window
pygame.display.set_mode((700, 500))
# Set the title of the display window
pygame.display.set_caption('CSW Basic pygame example')
# Get the surface of the window
surface = pygame.display.get_surface()

# Initialize game specific variables
black = pygame.Color('black')
white = pygame.Color('white')
ball = pygame.image.load("intro_ball.gif")
ballRect = ball.get_rect()

speed = [2, 2]
game = True

# Play the game till user quit
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[K_r]:
                ballRect.x = random.randint(0, surface.get_width()-ballRect.width)
                ballRect.y = random.randint(0, surface.get_height()-ballRect.height)

    # Update the ball
    ballRect = ballRect.move(speed)
    if ballRect.left < 0 or ballRect.right > surface.get_width():
        speed[0] = -speed[0]        # Bounce off the left or right wall
    if ballRect.top < 0 or ballRect.bottom > surface.get_height():
        speed[1] = -speed[1]        # Bounce off the top or bottom wall

    # Update the screen
    surface.fill(black)
    font = pygame.font.Font('freesansbold.ttf', 45)
    text = font.render("Welcome to CSW Basic pygame", False, white)
    surface.blit(text, ((surface.get_width()-text.get_width())/2, 0))
    surface.blit(ball, ballRect)
    pygame.display.update()

# Quit pygame and clean pygame window
pygame.quit()
