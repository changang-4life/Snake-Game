import pygame

pygame.init() # initialises (starts) all pygame modules so they are ready

# creating the screen / surface:
screen = pygame.display.set_mode((1000, 720))

# customising screen icon and caption:
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption('Snake Game - By Jade')

# Colours (in RGB):
black = (29, 29, 31) # for text
white = (255, 255, 255) # for screen colour when game is over
red = (255, 79, 79) # for snake
green = (146, 245, 113) # for food / apple

# Fonts:
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)

# Snake Coordinates
    # As you move to the right, the x value increases
    # As you move down, the y value increases

snake_x = 490
snake_y = 350

pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    # parametres: surface (i.e., screen), colour, xy coords (location), width  and height (i.e., 20 x 20)

pygame.display.update() # updates the display to include changes (rectangle)

# Allows the game to run forever until the user closes the window themselves
quit_game = False
while not quit_game:
    for event in pygame.event.get():
        # Gets a list of some possible events a user might do
        if event.type == pygame.QUIT:
            # checks for a quit event
            quit_game = True

pygame.quit()
quit()



