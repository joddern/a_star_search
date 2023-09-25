import heapq


class Node:
    def __init__(self, x, y, wall=False):
        self.x, self.y = x, y
        self.wall = wall


def find_neighbors_in_grid(grid, walls, x, y):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (
                y + i >= 0
                and y + i < len(grid)
                and x + j >= 0
                and x + j < len(grid[0])
                and (x + j, y + j) not in walls
                and (x + j, y + i) != (x, y)
            ):
                neighbors.append(x + j, y + i)
    return neighbors


def h(n):
    pass


