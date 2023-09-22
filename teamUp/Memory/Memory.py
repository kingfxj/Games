# When the game starts, a 525 by 425 pixel window is displayed with title Memory. A 4 by 4 grid with 16 tiles is
# displayed covering the left side of the window. Each tile has a 100 by 100 pixel image, bounded by a 5 pixels black
# border. There are 8 pairs of identical images, 16 images in total. For each new game, the tile images are randomly
# placed into the tiles. At the start of the game, all tiles are hidden by a covering image that is blue with a red
# question mark, bounded by a 3 pixels white border. A black rectangle, about 100 pixels wide and 425 pixels high,
# completes the window on the right. The time, in seconds, since the game started is displayed on the top right corner
# of the window in white font about 50 pixels high. When the player clicks on a hidden tile, the tile image is exposed.
# When the player clicks on a second tile hidden by the covering image, the tile image of the second tile is also
# exposed. If the two tile images match, the two tiles are permanently exposed. The player can continue clicking on
# other hidden tiles to search for matching tile images. If the two tile images do not match, both exposed tiles are
# hidden by the covering image after a delay of about half a second. Then, the player can continue clicking on hidden
# tiles to search for matching tile images. If the player clicks outside of a hidden tile, the click is ignored. The
# process of exposing tiles continues until all 8 pairs of tiles are permanently exposed. When this happens the game
# ends and the timer stops incrementing. When the player clicks on the close box, the window closes.


# How to load and blit image
import pygame, random


# User-defined functions
def main():
   # initialize all pygame modules (some need initialization)
   pygame.init()
   # create a pygame display window
   pygame.display.set_mode((525, 425))
   # set the title of the display window
   pygame.display.set_caption('Memory 3')   
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
   # An object in this class represents a complete game.
   def __init__(self, surface):
      # Initialize a Game.
      # - self is the Game to initialize
      # - surface is the display window surface object

      # === objects that are part of every game that we will discuss
      self.surface = surface
      self.bg_color = pygame.Color('black')
      
      self.FPS = 60
      self.game_Clock = pygame.time.Clock()
      self.close_clicked = False
      self.continue_game = True
      self.elapsed_time = 0
      
      # === game specific objects
      self.board = []
      self.board_size = 4
      self.create_board()
      self.occupied_tiles = 0
      self.tile1 = None
      self.tile2 = None

   def create_board(self):
      Tile.set_surface(self.surface)
      #width = self.surface.get_width()//self.board_size
      #height = self.surface.get_height()//self.board_size
      image = pygame.image.load('image0.bmp')
      width = image.get_width()
      height = image.get_height()
      image = []
      for i in range(1, 9):
         image.append(pygame.image.load('image'+str(i)+'.bmp'))
      image += image
      random.shuffle(image)
      for row_index in range(0, self.board_size):
         row = []
         for col_index in range(0,self.board_size):
            x = (width + 5) * col_index + 5
            y = (height + 5) * row_index + 5
            tile = Tile(x,y,image[row_index*self.board_size+col_index])
            row.append(tile)
         self.board.append(row)

   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
         # play frame
         self.handle_events()
         self.draw()            
         if self.continue_game:
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
         elif event.type == pygame.MOUSEBUTTONUP and self.continue_game:
             self.handle_mouse_up(event)

   def handle_mouse_up(self, event):
      # Respond to the player releasing the mouse button by
      # taking appropriate actions.
      # - self is the Game where the mouse up occurred
        for row in self.board:
            for tile in row:
                if tile.select(event.pos):
                    if not self.tile1:
                        self.tile1 = tile
                    else:
                        self.tile2 = tile
                    self.occupied_tiles = self.occupied_tiles + 1
                    return

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.surface.fill(self.bg_color) # clear the display surface first
      # Draw the tiles
      for each_row in self.board:
         for each_tile in each_row:
            each_tile.draw()
            self.draw_score()
      pygame.display.update() # make the updated surface appear on the display

   def draw_score(self):
      font = pygame.font.SysFont('', 70)
      text_box = font.render(str(self.elapsed_time), True, pygame.Color('white'), self.bg_color)
      x = self.surface.get_width() - text_box.get_width()
      y = 0
      self.surface.blit(text_box, (x, y))

   def update(self):
      # Update the game objects for the next frame.
      # - self is the Game to update
      if self.continue_game:
         self.elapsed_time = pygame.time.get_ticks() // 1000
      if self.tile1 and self.tile2:
         pygame.time.wait(500)
         if self.tile1 != self.tile2:
             self.occupied_tiles = self.occupied_tiles - 2
         self.tile1 = None
         self.tile2 = None

   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      if self.occupied_tiles == self.board_size ** 2:
         self.continue_game = False


class Tile:
   # An object in this class represents a Dot that moves 
   # Shared Attrbutes or Class Attributes
   surface = None
   border_size = 3
   border_color = pygame.Color('white')
   question = pygame.image.load('image0.bmp')

   @classmethod
   def set_surface(cls,game_surface):
      cls.surface = game_surface

   # Instance Methods
   def __init__(self,x,y,image):
      self.image = image
      self.occupied = False
      width = self.image.get_width()
      height = self.image.get_height()
      self.rect = pygame.Rect(x,y,width,height)

   def draw(self):
      # Draw the dot on the surface
      # - self is the Dot
      pygame.draw.rect(Tile.surface,Tile.border_color,self.rect,Tile.border_size)
      if self.occupied:
         Tile.surface.blit(self.image,self.rect)
      else:
         Tile.surface.blit(self.question, self.rect)

   def select(self, mouse_position):
      if self.rect.collidepoint(mouse_position[0], mouse_position[1]) and not self.occupied:
         self.occupied = True
         return self.occupied

   def __eq__(self, other):
      if self.image == other.image:
         return True
      else:
         self.occupied = False
         other.occupied = False
         return False


main()