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
FOOD_COUNT = 4
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Courier New', 20)
game_over_text = ""
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
BLUE = (0, 0, 255)
# Define the Snake class
class Snake:
    def __init__(self, colour, start_direction):
        self.x = GRID_RADIUS * 2 * (NUMCOLS/2) + GRID_RADIUS  # The snake1 must be on the grid
        self.y = GRID_RADIUS * 2 * (NUMROWS/2) + GRID_RADIUS
        self.direction = start_direction
        self.length = 1
        self.body = []
        self.colour = colour
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
            pygame.draw.circle(window, self.colour, (part[0], part[1]), GRID_RADIUS)
    def check_collision(self, other_snake):
        # Collision with border
        if self.x < 0 or self.x >= window_width or self.y < 0 or self.y >= window_height:
            return True
        # Collision with self
        for part in self.body[1:]:
            if self.x == part[0] and self.y == part[1]:
                return True
        # Collision with other snake
        for part in other_snake.body[1:]:
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

def initialiseGame():
    # Initialize the snake1 and food
    init_food_list = []
    for n in range(FOOD_COUNT):
        init_food_list.append(Food())
    return Snake(GREEN, "RIGHT"), Snake(BLUE, "LEFT"), init_food_list

snake1, snake2, food_list = initialiseGame()

# Game loop
running = True
game_over = False
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Game over logic
            if game_over:
                if event.key == pygame.K_r:
                    game_over = False
                    snake1, snake2, food_list = initialiseGame()
                elif event.key == pygame.K_q:
                    running = False
            # Snake 1
            if event.key == pygame.K_UP and snake1.direction != "DOWN":
                snake1.direction = "UP"
            elif event.key == pygame.K_DOWN and snake1.direction != "UP":
                snake1.direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake1.direction != "RIGHT":
                snake1.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake1.direction != "LEFT":
                snake1.direction = "RIGHT"
            # Snake 2
            if event.key == pygame.K_w and snake2.direction != "DOWN":
                snake2.direction = "UP"
            elif event.key == pygame.K_s and snake2.direction != "UP":
                snake2.direction = "DOWN"
            elif event.key == pygame.K_a and snake2.direction != "RIGHT":
                snake2.direction = "LEFT"
            elif event.key == pygame.K_d and snake2.direction != "LEFT":
                snake2.direction = "RIGHT"
    if not game_over:
        # Move the snakes
        snake1.move()
        snake2.move()
        # Check collision with food
        for food in food_list:
            if snake1.x == food.x and snake1.y == food.y:
                snake1.length += 1
                food_list.remove(food)  # Remove the food from the list
                food_list.append(Food())  # Add a new food to the list at a new location
            if snake2.x == food.x and snake2.y == food.y:
                snake2.length += 1
                food_list.remove(food)  # Remove the food from the list
                food_list.append(Food())  # Add a new food to the list at a new location
        # Update the snake1's body
        snake1.body.insert(0, (snake1.x, snake1.y))
        # Update the snake2's body
        snake2.body.insert(0, (snake2.x, snake2.y))
        if len(snake1.body) > snake1.length:
            snake1.body.pop()
        if len(snake2.body) > snake2.length:
            snake2.body.pop()
        # Check collision with snake1's body or boundaries
        if snake1.check_collision(snake2):
            game_over = True
            game_over_text = "Blue is the winner!"
        if snake2.check_collision(snake1):
            game_over = True
            game_over_text = "Green is the winner!"
        if (snake1.x, snake1.y) == (snake2.x, snake2.y):
            game_over = True
            game_over_text = "Nobody won."
        # Clear the window
        window.fill(BLACK)
        # Draw the snakes and food
        snake1.draw()
        snake2.draw()
        for food in food_list:
            food.draw()
    else:  # Game over
        window.fill(BLACK)
        text_surface = my_font.render(game_over_text, False, WHITE)
        text_rect = text_surface.get_rect(center=(window_width // 2, window_height // 2 - 60))  # Position the text
        window.blit(text_surface, text_rect)  # Draw the text on the screen

        text_surface = my_font.render(f"Score green: {snake1.length}", False, WHITE)
        text_rect = text_surface.get_rect(center=(window_width // 2, window_height // 2 - 30))  # Position the text
        window.blit(text_surface, text_rect)  # Draw the text on the screen

        text_surface = my_font.render(f"Score blue: {snake2.length}", False, WHITE)
        text_rect = text_surface.get_rect(center=(window_width // 2, window_height // 2))  # Position the text
        window.blit(text_surface, text_rect)  # Draw the text on the screen

        text_surface = my_font.render("q to quit, r to retry", False, WHITE)
        text_rect = text_surface.get_rect(center=(window_width // 2, window_height // 2 + 30))  # Position the text
        window.blit(text_surface, text_rect)  # Draw the text on the screen


    # Update the display
    pygame.display.update()
    # Set the game speed
    clock.tick(FPS)
# Quit the game
pygame.quit()
