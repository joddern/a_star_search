import pygame
import sys

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Grid:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = [[0] * width for _ in range(height)]  # Initialize with open spaces
        self.start = (0, 0)
        self.goal = (width - 1, height - 1)
        self.walls = []

    def toggle_wall(self, x, y, wall_mode):
        if (x, y) == self.start or (x, y) == self.goal:
            return
        if not wall_mode:
            if (x, y) in self.walls:
                self.walls.remove((x, y))
        else:
            if (x, y) not in self.walls:
                self.walls.append((x, y))

    def set_start(self, x, y):
        self.start = (x, y)

    def set_goal(self, x, y):
        self.goal = (x, y)

    def is_cell_wall(self, x, y):
        return (x, y) in self.walls

    def draw(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                if (x, y) == self.start:
                    pygame.draw.rect(screen, GREEN, rect)
                elif (x, y) == self.goal:
                    pygame.draw.rect(screen, RED, rect)
                elif (x, y) in self.walls:
                    pygame.draw.rect(screen, BLACK, rect)
                else:
                    pygame.draw.rect(screen, WHITE, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)

def main():
    pygame.init()

    # Define grid parameters
    width = 20
    height = 15
    cell_size = 30

    grid = Grid(width, height, cell_size)

    # Set up Pygame window
    screen = pygame.display.set_mode((width * cell_size, height * cell_size))
    pygame.display.set_caption("Grid Environment")

    running = True
    drawing_wall = False
    set_walls = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    x, y = event.pos
                    x //= cell_size
                    y //= cell_size
                    set_walls = not grid.is_cell_wall(x, y)
                    grid.toggle_wall(x, y, set_walls)
                    drawing_wall = True
                elif event.button == 3:  # Right click
                    x, y = event.pos
                    x //= cell_size
                    y //= cell_size
                    grid.set_start(x, y)
                elif event.button == 2:  # Middle click
                    x, y = event.pos
                    x //= cell_size
                    y //= cell_size
                    grid.set_goal(x, y)
            elif event.type == pygame.MOUSEMOTION:
                if drawing_wall:
                    x, y = event.pos
                    x //= cell_size
                    y //= cell_size
                    grid.toggle_wall(x, y, set_walls)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    drawing_wall = False

        grid.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
