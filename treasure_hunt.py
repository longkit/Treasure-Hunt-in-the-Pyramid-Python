import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 50
ROWS, COLS = HEIGHT // TILE_SIZE, WIDTH // TILE_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Hunt in the Pyramid")

# Fonts
font = pygame.font.Font(None, 36)

# Initialize game elements
treasure = None
trapper = None
player = None
visited = set()
path = []

# Directions (dx, dy) for moving: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Generate a random position for an element
def random_position():
    return random.randint(0, ROWS - 1), random.randint(0, COLS - 1)

# Check if a position is within bounds and not blocked
def is_valid(pos, traps):
    x, y = pos
    return 0 <= x < ROWS and 0 <= y < COLS and pos not in traps

# Draw the grid and elements
def draw_grid(traps, treasure, player):
    screen.fill(WHITE)

    # Draw grid
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

    # Draw traps
    for trap in traps:
        x, y = trap
        pygame.draw.rect(screen, RED, (y * TILE_SIZE, x * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw treasure
    tx, ty = treasure
    pygame.draw.rect(screen, BLUE, (ty * TILE_SIZE, tx * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw player
    px, py = player
    pygame.draw.rect(screen, GREEN, (py * TILE_SIZE, px * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.flip()

# Breadth-First Search to find the shortest path
def find_path(player, treasure, traps):
    queue = [(player, [])]
    visited = set()

    while queue:
        current, path = queue.pop(0)

        if current == treasure:
            return path

        if current in visited:
            continue

        visited.add(current)

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if is_valid(neighbor, traps):
                queue.append((neighbor, path + [neighbor]))

    return []

# Game initialization
def initialize_game():
    global treasure, player, traps, path

    traps = set()
    player = random_position()
    treasure = random_position()

    # Generate traps
    while len(traps) < (ROWS * COLS) // 5:
        trap = random_position()
        if trap != player and trap != treasure:
            traps.add(trap)

    # Find path
    path = find_path(player, treasure, traps)

# Main game loop
def main():
    clock = pygame.time.Clock()
    initialize_game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if path:
            next_step = path.pop(0)
            global player
            player = next_step

        draw_grid(traps, treasure, player)
        clock.tick(5)

        # Check win condition
        if player == treasure:
            print("You found the treasure!")
            pygame.time.delay(2000)
            initialize_game()

if __name__ == "__main__":
    main()
