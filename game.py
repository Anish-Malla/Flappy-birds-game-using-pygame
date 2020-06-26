# Import and initialize the pygame library
import pygame
import random

pygame.init()

# Set up the drawing window
SCREEN = pygame.display.set_mode((500, 750))

# BACKGROUND
BACKGROUND = pygame.image.load('background.jpg')

# PLAYER
BIRD_IMAGE = pygame.image.load('bird1.png')
bird_x = 50
bird_y = 300
bird_y_change = 0

# OBSTACLES
OBSTACLE_WIDTH = 70
OBSTACE_X_CHANGE = 4
obstacle_x = 500
# def randomX():
#     oh = random.randint(200,400)
#     return oh
OBSTACLE_HEIGHT = random.randint(150,450)
OBSTACLE_COLOR = (211, 253, 117)

font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

max_scores = [0]

game_over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over():
    maximum = max(max_scores)
    overttext = game_over_font.render(f"GAME OVER", True, (200,35,35))
    SCREEN.blit(overttext, (50, 300))
    overttext2 = font.render(f"SCORE: {score_value} MAX SCORE: {maximum}", True, (255, 255, 255))
    SCREEN.blit(overttext2, (50, 400))
    if score_value == maximum:
        overttext3 = font.render(f"NEW HIGH SCORE!!", True, (200,35,35))
        SCREEN.blit(overttext3, (50, 100))

def score_display(x,y):
    score = font.render(f"Score: {score_value}", True, (255,255,255))
    SCREEN.blit(score, (x,y))
    
def obstacle(obstacle_x, obstacle_height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, obstacle_height))
    bottom_obstacle_height = 635 - obstacle_height - 150
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 635, OBSTACLE_WIDTH, -bottom_obstacle_height))

def player(x, y):
    SCREEN.blit(BIRD_IMAGE, (x,y))

# COLLISION DETECTION
def collision_bool(obstacle_x, obstacle_height, bird_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50 + 64):
        if bird_y <= obstacle_height or bird_y >= (bottom_obstacle_height - 64):
            return True
    return False

startFont = pygame.font.Font('freesansbold.ttf', 32)
def start():
    overttext2 = startFont.render(f"SPACE BAR TO START", True, (255, 255, 255))
    SCREEN.blit(overttext2, (50, 200))
    pygame.display.update()

# Run until the user asks to quit
running = True
flag = False
waiting = True
collision = False

while running:
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(BACKGROUND, (0, 0))

    while waiting:
        if collision:
            game_over()
            start()
        else:
            start()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score_value = 0
                    bird_y = 300
                    obstacle_x = 500
                    waiting = False

            if event.type == pygame.QUIT:
                waiting = False
                running = False

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            waiting = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = 6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = -3

    bird_y -= bird_y_change

    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 571:
        bird_y = 571

    obstacle_x -= OBSTACE_X_CHANGE

    collision = collision_bool(obstacle_x, OBSTACLE_HEIGHT, bird_y, OBSTACLE_HEIGHT + 150)

    if collision:
        max_scores.append(score_value)
        game_over()
        waiting = True
    else:
        if obstacle_x <= -10:
            obstacle_x = 500
            OBSTACLE_HEIGHT = random.randint(200,400)
            obstacle(obstacle_x, OBSTACLE_HEIGHT)
            score_value += 1
        player(bird_x, bird_y)
        obstacle(obstacle_x, OBSTACLE_HEIGHT)

    score_display(textX,textY)
    pygame.display.update()

# Done! Time to quit.
pygame.quit()