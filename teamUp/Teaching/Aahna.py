import pygame

def main():
    pygame.init()
    pygame.display.set_mode((900,800))
    pygame.display.set_caption('CSW Pong Final Project')
    surface = pygame.display.get_surface()
    play_game(surface)
    #pygame.quit()
    ball = pygame.image.load('intro_ball.gif')
    #ballRect = ball.get_rect()
    black = pygame.Color('black')
    surface.fill(black)
    font = pygame.font.Font('freesansbold.ttf', 24)
    pygame.display.update()
    pygame.quit()

'''
Class
of
Start
Button
'''

class Button:
    def __init__(self, text, position, surface, font, bg="black"):
        self.x, self.y = position
        self.font = pygame.font.Font("freesansbold", 25)
        self.text = self.font.render(text, 1, pygame.Color('white'))
        self.surface = surface
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.circle = pygame.Circle(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        self.surface.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pose()
        if event.type == pygame.mousebuttondown:
            if pygame.mouse.get_pressed()[0]:
                if self.circle.collidepoint(x, y):
                    self.init(bg='green')

'''
Class of ball
'''

class Ball:
    def __init__(self, surface, color, center, velocity, radius, score):
        self.surface = surface
        self.color = color
        self.center = center
        self.velocity = velocity
        self.radius = radius
        self.score = score

    def move(self):
        for coordinate in range(2):
            self.center[coordinate] += self.velocity[coordinate]

    def display(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

'''
Game
'''
def play_game(surface):
    opened = True
    winner = 0
    background = pygame.Color('black')
    wordColor = pygame.Color('white')

    score = []

    '''
    Challenge 1
    Randomize the initial y position of the ball
    '''

    ball = Ball(surface, wordColor, [300, 250], [3, 6], 10, score)
    pygame.key.set_repeat(30,30)

    backgroundColor = 'black'

    while opened:
        opened = control_game(opened)
        if not winner:
            ball.move()


            game_screen(surface, backgroundColor, ball)
        winner = is_game_finished()

# import random
# value = random.uniform(0,1)
#
# while opened:
#     opened = control_game(opened)
#     ball = value = random.uniform(0,1)

'''
Challenge 4
Make an AI racket
'''

def control_game(opened):
    # Control the movement of the paddle according to player's input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            opened = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()  # Record the keys that are pressed
            if keys[pygame.K_q]:
                # Key q is pressed
                pass
            if keys[pygame.K_a]:
                # Key a is pressed
                pass
            # if event.key == K_u:
            #     keys[] = True
    return opened


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


if __name__ == "__main__":
    main()
