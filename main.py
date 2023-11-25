'''
Greedy Snake Game
'''
import random
import pygame
# Initialize the game
pygame.init()
# Define game variables
GRID_RADIUS = 10
FPS = 5
NUMCOLS = 30
NUMROWS = 20
clock = pygame.time.Clock()
# Set up the game window
window_width = NUMCOLS * (GRID_RADIUS * 2)  # NUM COLS/ROWS next to each other
window_height = NUMROWS * (GRID_RADIUS * 2)
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Greedy Snake Game")
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
# Define the Snake class
class Snake:
    def __init__(self):
        self.x = GRID_RADIUS * 2 * (NUMCOLS/2) + GRID_RADIUS  # The snake must be on the grid
        self.y = GRID_RADIUS * 2 * (NUMROWS/2) + GRID_RADIUS
        self.direction = "RIGHT"
        self.length = 1
        self.body = []
    def move(self):
        if self.direction == "UP":
            self.y -= GRID_RADIUS * 2
        elif self.direction == "DOWN":
            self.y += GRID_RADIUS * 2
        elif self.direction == "LEFT":
            self.x -= GRID_RADIUS * 2
        elif self.direction == "RIGHT":
            self.x += GRID_RADIUS * 2
    def draw(self):
        for part in self.body:
            pygame.draw.circle(window, GREEN, (part[0], part[1]), GRID_RADIUS)
    def check_collision(self):
        if self.x < 0 or self.x >= window_width or self.y < 0 or self.y >= window_height:
            return True
        for part in self.body[1:]:
            if self.x == part[0] and self.y == part[1]:
                return True
        return False
# Define the Food class
class Food:
    def __init__(self):
        # Random position in the grid
        self.x = random.randint(
            0, (window_width - GRID_RADIUS) // (GRID_RADIUS * 2)) * (GRID_RADIUS * 2) + GRID_RADIUS
        self.y = random.randint(
            0, (window_height - GRID_RADIUS) // (GRID_RADIUS * 2)) * (GRID_RADIUS * 2) + GRID_RADIUS
    def draw(self):
        pygame.draw.circle(window, RED, (self.x, self.y), GRID_RADIUS)
# Initialize the snake and food
snake = Snake()
food = Food()
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "DOWN":
                snake.direction = "UP"
            elif event.key == pygame.K_DOWN and snake.direction != "UP":
                snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                snake.direction = "RIGHT"
    # Move the snake
    snake.move()
    # Check collision with food
    if snake.x == food.x and snake.y == food.y:
        snake.length += 1
        food = Food()
    # Update the snake's body
    snake.body.insert(0, (snake.x, snake.y))
    if len(snake.body) > snake.length:
        snake.body.pop()
    # Check collision with snake's body or boundaries
    if snake.check_collision():
        running = False
    # Clear the window
    window.fill(BLACK)
    # Draw the snake and food
    snake.draw()
    food.draw()
    # Update the display
    pygame.display.update()
    # Set the game speed
    clock.tick(FPS)
# Quit the game
pygame.quit()
