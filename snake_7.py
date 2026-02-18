import pygame
import time
import random
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
green = (146, 245, 113) # for background
yellow = (252, 241, 116) # for food

# Fonts:
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

def message(msg, txt_colour):
    txt = msg_font.render(msg, True, txt_colour)

    text_box = txt.get_rect(center = (500, 360))
    screen.blit(txt, text_box)


# Snake Coordinates
    # As you move to the right, the x value increases
    # As you move down, the y value increases


clock = pygame.time.Clock()

def game_loop():
    # Allows the game to run forever until the user closes the window themselves
    
    
# random x coords for food:
    food_x = round(random.randrange(20, 1000 - 20)/20) * 20
    food_y = round(random.randrange(20, 720 - 20)/20) * 20
    
    quit_game = False
    game_over = False

    snake_x = 490
    snake_y = 350

    snake_x_change = 0
    snake_y_change = 0

    while not quit_game:
        while game_over: # while game_over = True
            # Function gives user the option to quit or play again when they die
            screen.fill(white)
            message("You died! Press 'Q' to Quit or 'A' to play again.",    black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop() # Restart the main game loop
                        
        for event in pygame.event.get():
            # Gets a list of some possible events a user might do
            if event.type == pygame.QUIT:
                # checks for a quit event
                quit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake_x_change = -20
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    snake_x_change = 20
                    snake_y_change = 0
                elif event.key  == pygame.K_UP or event.key == pygame.K_w:
                    snake_x_change = 0
                    snake_y_change = -20
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    snake_x_change = 0
                    snake_y_change = 20
        
        if snake_x >= 1000 or snake_x < 0 or snake_y >= 720 or snake_y < 0:
            game_over = True
        
        snake_x += snake_x_change
        snake_y += snake_y_change

        screen.fill(green)

        pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
            # parametres: surface (i.e., screen), colour, xy coords (location), width  and height (i.e., 20 x 20)

        pygame.draw.circle(screen, yellow, [food_x, food_y], 10)

        pygame.display.update() # updates the display to include changes (rectangle)
            
        if snake_x == food_x - 10 and snake_y == food_y - 10:
            # random x coords for food:
            food_x = round(random.randrange(20, 1000 - 20)/20)* 20
            food_y = round(random.randrange(20, 720 - 20)/20)* 20


        clock.tick(10) # waits 10 ticks before restarting the while loop.
            # snake continually moves 20 pixels every 10 ticks

    pygame.quit()
    quit()

# Main routine
game_loop()