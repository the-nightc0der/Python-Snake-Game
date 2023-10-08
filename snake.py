import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rohit's Snake Game")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Snake variables
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]  # Initial snake position
snake_direction = (0, 0)  # Initial snake direction (no movement)
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))  # Initial food position
score = 0  # Player's score

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Check for arrow key presses to change snake's direction
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)  # Move up
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)  # Move down
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)  # Move left
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)  # Move right

    # Update snake position
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

    # Wrap around the screen
    new_head = (new_head[0] % GRID_WIDTH, new_head[1] % GRID_HEIGHT)

    snake.insert(0, new_head)  # Add new head to the snake's body

    # Check for collisions with food
    if snake[0] == food:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        score += 1
    else:
        snake.pop()  # Remove the tail segment

    # Draw everything on the screen
    screen.fill(BLACK)  # Clear the screen

    # Draw the snake and food as rectangles
    for segment in snake:
        pygame.draw.rect(
            screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        )

    pygame.draw.rect(
        screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    )

    # Display the player's score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (10, 10))

    pygame.display.update()  # Update the display

    # Control the frame rate to make the game run at a consistent speed
    clock.tick(10)  # Set the frame rate to 10 frames per second
