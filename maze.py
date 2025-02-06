import numpy as np
import matplotlib.pyplot as plt
import time
import random

# Define the maze (0 = path, 1 = wall)
maze = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
])

# Randomly select start position
empty_spaces = [(x, y) for x in range(maze.shape[0]) for y in range(maze.shape[1]) if maze[x, y] == 0]
start = random.choice(empty_spaces)
goal = (5, 6)


def is_valid_move(maze, pos):
    """Check if the move is valid (inside maze and not a wall)."""
    x, y = pos
    return 0 <= x < maze.shape[0] and 0 <= y < maze.shape[1] and maze[x, y] == 0


def solve_maze(maze, start, goal):
    """Solve the maze using DFS."""
    stack = [start]  # Stack for DFS
    visited = set()
    path = []

    while stack:
        pos = stack.pop()

        if pos in visited:
            continue

        visited.add(pos)
        path.append(pos)

        if pos == goal:
            return path  # Solution found

        # Possible moves in random order
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(moves)

        for move in moves:
            new_pos = (pos[0] + move[0], pos[1] + move[1])
            if is_valid_move(maze, new_pos) and new_pos not in visited:
                stack.append(new_pos)

    return None  # No solution


def display_maze(maze, path):
    """Display the maze and the solution path."""
    display = np.copy(maze)

    for pos in path:
        display[pos] = 2  # Mark the path

    plt.imshow(display, cmap='gray_r')
    plt.xticks([])
    plt.yticks([])
    plt.show()


# Solve the maze
solution = solve_maze(maze, start, goal)

if solution:
    print("Path found:", solution)
    display_maze(maze, solution)
else:
    print("No path found.")
