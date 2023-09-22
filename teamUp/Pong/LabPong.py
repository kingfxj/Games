# In the full final of the game: If the ball hits the right edge of the window, the upper-left score
# will be added one. If the ball hits the left edge of the window, the upper-right score will be
# added one. If the ball hits the upper edge or lower edge of the window, scores will not
# change. When the ball hits the edge of the window or paddles, the ball bounces from the
# window edges, following the law of reflection: Angle of incidence equals to angle of reflection.
# The paddle are controlled by two players respectively. The left-side paddle is controlled by
# the q key and the a key. When the player presses and holds the q key, the paddle moves up.
# When the player presses and holds the a key, the paddle moves down. The right-side paddle
# is controlled by the p key and the I key. When the player presses and holds the p key, the
# paddle moves up. When the player presses and holds the I key, the paddle moves down.


import pygame
from pygame.locals import *


# User-defined functions
def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((600, 500))
    # set the title of the display window
    pygame.display.set_caption('Pong 3')
    # get the display surface
    w_surface = pygame.display.get_surface()
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play()
    # quit pygame and clean up the pygame window
    pygame.quit()


# User-defined classes
class Game:
    # An object in this class represents a complete game.\
    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object
        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')
        self.fg_color = 'white'
        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True
        pygame.key.set_repeat(30, 30)

        # === game specific objects
        self.score = [0, 0]
        self.circle = Circle(self.fg_color, 10, [200, 200], [3, 6], surface, self.score)
        self.paddles = [pygame.Rect(100, 200, 10, 100), pygame.Rect(500, 200, 10, 100)]
        self.max_frames = 150
        self.frame_counter = 0

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.
        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()
            if self.continue_game:
                # Shows things
                self.update()
                self.decide_continue()
            self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second

    def handle_events(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            elif event.type == KEYDOWN:
                if self.continue_game:
                    paddle_increment = 10
                    list_of_keys = pygame.key.get_pressed()                    # Record the keys that are pressed
                    if list_of_keys[K_q]:
                        if self.paddles[0].top >= 0:                             # The left paddle is in the window
                            self.paddles[0].move_ip(0, -paddle_increment)         # Move the paddle down
                    if list_of_keys[K_a]:
                        if self.paddles[0].bottom <= self.surface.get_height():   # The left paddle is in the window
                            self.paddles[0].move_ip(0, paddle_increment)          # Move the paddle up
                    if list_of_keys[K_p]:
                        if self.paddles[1].top >= 0:                             # The right paddle is in the window
                            self.paddles[1].move_ip(0, -paddle_increment)         # Move the paddle down
                    if list_of_keys[K_l]:
                        if self.paddles[1].bottom <= self.surface.get_height():   # The right paddle is in the window
                            self.paddles[1].move_ip(0, paddle_increment)          # Move the paddle up

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw
        self.surface.fill(self.bg_color) # clear the display surface first
        self.circle.draw()
        for paddle in self.paddles:
            pygame.draw.rect(self.surface, pygame.Color(self.fg_color), paddle)
        text1 = pygame.font.Font('freesansbold.ttf', 70).render(str(self.score[0]), True, pygame.Color(self.fg_color), self.surface)
        text2 = pygame.font.Font('freesansbold.ttf', 70).render(str(self.score[1]), True, pygame.Color(self.fg_color), self.surface)
        self.surface.blit(text1, (0, 0))
        self.surface.blit(text2, (self.surface.get_width()-text2.get_width(), 0))
        pygame.display.update() # make the updated surface appear on the display

    def update(self):
        # Update the game objects.
        # - self is the Game to update
        self.circle.move()
        self.circle.bounce(self.paddles)
        self.frame_counter = self.frame_counter + 1

    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        if (self.score[0] >= 11) or (self.score[1] >= 11):
            self.continue_game = False


class Circle:
    # An object in this class represents a Dot that moves
    def __init__(self, circle_color, circle_radius, circle_center, circle_velocity, surface, score):
        # Initialize a Dot.
        # - self is the Dot to initialize
        # - color is the pygame.Color of the dot
        # - center is a list containing the x and y int
        #   coords of the center of the dot
        # - radius is the int pixel radius of the dot
        # - velocity is a list containing the x and y components
        # - surface is the window's pygame.Surface object
        self.color = pygame.Color(circle_color)
        self.radius = circle_radius
        self.center = circle_center
        self.velocity = circle_velocity
        self.surface = surface
        self.score = score

    def move(self):
        # Change the location of the Dot by adding the corresponding
        # speed values to the x and y coordinate of its center
        # - self is the Dot
        size = self.surface.get_size()
        for coordinate in range(0, 2):
            self.center[coordinate] += self.velocity[coordinate]
            if self.center[coordinate] < self.radius or self.center[coordinate] + self.radius > size[coordinate]:
                self.velocity[coordinate] = -self.velocity[coordinate]      # Bounce of the walls

        if self.center[0] < self.radius:
            self.score[1] += 1
        if self.center[0] + self.radius > size[0]:
            self.score[0] += 1

    # Bounce off the paddles
    def bounce(self, paddles):
        for coordinate in range(0, len(paddles)):
            if paddles[coordinate].collidepoint(self.center):
                self.velocity[0] = (-1) ** coordinate * abs(self.velocity[0])

    def draw(self):
        # Draw the dot on the surface
        # - self is the Dot
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)


main()
