import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 1980
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the player size and move distance
player_size = 40
player_move_distance = player_size

# Set the player's starting position
player_x = screen_width // 2
player_y = screen_height // 2

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Define the map size and tile size
map_width = 50
map_height = 30
tile_size = 40

# Define the walls
WALL = 1
FLOOR = 0

# Define the map array
map_data = [[0 for y in range(map_height)] for x in range(map_width)]

# Generate the map data
for x in range(map_width):
    for y in range(map_height):
        if x == 0 or y == 0 or x == map_width - 1 or y == map_height - 1:
            map_data[x][y] = WALL
        elif random.random() < 0.3:
            map_data[x][y] = WALL

# Align the player position with the grid of tiles
player_x = ((player_x // tile_size) * tile_size) + ((tile_size - player_size) // 2)
player_y = ((player_y // tile_size) * tile_size) + ((tile_size - player_size) // 2)

# Set up the clock
clock = pygame.time.Clock()

# Set up the game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if player_y - player_move_distance >= 0 and map_data[player_x // tile_size][(player_y - player_move_distance) // tile_size] != WALL:
                    player_y -= player_move_distance
            elif event.key == pygame.K_a:
                if player_x - player_move_distance >= 0 and map_data[(player_x - player_move_distance) // tile_size][player_y // tile_size] != WALL:
                    player_x -= player_move_distance
            elif event.key == pygame.K_s:
                if player_y + player_move_distance < screen_height and map_data[player_x // tile_size][(player_y + player_move_distance) // tile_size] != WALL:
                    player_y += player_move_distance
            elif event.key == pygame.K_d:
                if player_x + player_move_distance < screen_width and map_data[(player_x + player_move_distance) // tile_size][player_y // tile_size] != WALL:
                    player_x += player_move_distance

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the map
    for x in range(map_width):
        for y in range(map_height):
            if map_data[x][y] == WALL:
                pygame.draw.rect(screen, GRAY, (x * tile_size, y * tile_size, tile_size, tile_size))

    # Draw the player
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(120)

# Quit Pygame
pygame.quit()
