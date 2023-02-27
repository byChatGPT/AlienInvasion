import pygame
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Alien Invasion")

# Set the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set the font
font = pygame.font.SysFont(None, 25)

# Set the game variables
player_x = WINDOW_WIDTH // 2
player_y = WINDOW_HEIGHT - 50
player_speed = 5
player_width = 50
player_height = 50

alien_x = random.randint(0, WINDOW_WIDTH - player_width)
alien_y = random.randint(50, 150)
alien_speed = 3
alien_width = 50
alien_height = 50

score = 0

# Main game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - player_width:
        player_x += player_speed

    # Move the alien
    alien_y += alien_speed
    if alien_y > WINDOW_HEIGHT:
        alien_x = random.randint(0, WINDOW_WIDTH - player_width)
        alien_y = random.randint(50, 150)
        score += 1

    # Check for collision
    if (alien_y + alien_height >= player_y and alien_y <= player_y + player_height) and (alien_x + alien_width >= player_x and alien_x <= player_x + player_width):
        alien_x = random.randint(0, WINDOW_WIDTH - player_width)
        alien_y = random.randint(50, 150)
        score -= 1

    # Draw the game objects
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (alien_x, alien_y, alien_width, alien_height))

    # Draw the score
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()

