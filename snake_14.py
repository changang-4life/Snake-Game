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
score_font = pygame.font.SysFont("snake chan.ttf", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

def message(msg, txt_colour):
    txt = msg_font.render(msg, True, txt_colour)

    text_box = txt.get_rect(center = (500, 360))
    screen.blit(txt, text_box)

clock = pygame.time.Clock()

# Function to keep track of the highest score - writes value to a file
def load_high_score():
    try:
        hi_score_file = open("HI_score.txt", "r")
    except IOError:
        hi_score_file = open("HI_score.txt", "w")
        hi_score_file.write("0")
    hi_score_file = open("HI_score.txt", "r")
    value = hi_score_file.read()
    hi_score_file.close()
    return value

# Function to update record of the highest score
def update_high_score(score, high_score):
    if int(score) > int(high_score):
        return score
    else:
        return high_score

# Save updated high score if player beats it
def save_high_score(high_score):
    high_score_file = open("Hi_score.txt", "w")
    high_score_file.write(str(high_score))
    high_score_file.close()

# Display player score throughout the game
def player_score(score, score_colour, hi_score):
    display_score = score_font.render(f"Score: {score}", True, score_colour)
    screen.blit(display_score, (800, 20)) # Coordinates for top right

    # High Score
    display_score = score_font.render(f"High Score: {hi_score}", True, score_colour)
    screen.blit(display_score, (10, 10)) # Coordinates for top left

def draw_snake(snake_list):
    print(f"Snake List: {snake_list}") # For testing purposes
    for i in snake_list:
        pygame.draw.rect(screen, red, [i[0], i[1], 20, 20])

def game_loop():
    # Random x coords for food:
    food_x = round(random.randrange(20, 1000 - 20)/20)* 20
    food_y = round(random.randrange(20, 720 - 20)/20)* 20

    # Loads the hgih score
    high_score = load_high_score()
    print(f"high_score test: {high_score}") # For testing purposes only

    # Allows the game to run forever until the user closes the window themselves
    quit_game = False
    game_over = False

    snake_x = 480
    snake_y = 340

    snake_x_change = 0
    snake_y_change = 0

    snake_list = []
    snake_length = 1

    while not quit_game:
        while game_over: # while game_over = True
            # Function gives user the option to quit or play again when they die
            save_high_score(high_score)
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
                instructions = "Exit: X again to Quit, SPACE to resume, R to reset"
                message(instructions, white)
                pygame.display.update()
                # checks for a quit event
                
                end = False
                while not end: # while end = False
                    for event in pygame.event.get():
                        # If user presses X button, game quits:
                        if event.type == pygame.QUIT:
                            quit_game = True
                            end = True
                        
                        # If user presses 'R' button again, game resets
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                end = True, game_loop()
                        
                        # If user presses the space-bar, game continues
                            if event.key == pygame.K_SPACE:
                                end = True
                        
                        # If user presses 'Q', game quits
                            if event.key == pygame.K_q:
                                quit_game = True
                                end = True

            # Handles snake movement:
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

        # Creates snake (replaces simple rectangle in previous version)
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True
        
        draw_snake(snake_list)

        # Keeping track of the player's score
        score = snake_length - 1 # score excludes snake's head
        player_score(score, black, high_score)

        high_score = update_high_score(score, high_score)

        # Links speed of snake to player score to increase difficulty
        if score > 3:
            speed = score
        else:
            speed = 3

        # Using a sprite (previously, the yellow circle) to represent food)
        food = pygame.Rect(food_x, food_y, 20, 20)
        apple = pygame.image.load("apple_3.png").convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple, [20, 20])
        screen.blit(resized_apple, food)

        pygame.display.update() # Updates the display to include changes (rectangle)

        if snake_x == food_x and snake_y == food_y:
            # Random x coords for food:
            food_x = round(random.randrange(20, 1000 - 20)/20)* 20
            food_y = round(random.randrange(20, 720 - 20)/20)* 20

            # For testing purposes
            print("Got it!")

            # Increases length of snake (by original size)
            snake_length += 1

        # Sets the speed at which each iteration of the game loop runs in frames per second. In this case, it is set to 10fps.
        clock.tick(speed)

    pygame.quit()
    quit()

# Main routine
game_loop()