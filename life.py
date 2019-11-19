import numpy as np


def start_game(seed, grid_rows=10, grid_cols=10):
    grid = np.zeros(shape=(grid_rows, grid_cols), dtype=bool)
    r = int(grid_rows / 2 - seed.shape[0] / 2)
    c = int(grid_cols / 2 - seed.shape[1] / 2)
    grid[r:r + seed.shape[0], c:c + seed.shape[1]] = seed
    return grid


def count_neighbours(grid, row, col):
    from_row = max(row - 1, 0)
    from_col = max(col - 1, 0)
    to_row = min(row + 2, grid.shape[0] - 1)
    to_col = min(col + 2, grid.shape[1] - 1)
    num_neighbours = np.count_nonzero(grid[from_row:to_row, from_col:to_col])
    return num_neighbours - grid[row, col]


def is_alive(grid, row, col):
    """
    1. Any live cell with two or three neighbors survives.
    2. Any dead cell with three live neighbors becomes a live cell.
    3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    """
    num_neighbours = count_neighbours(grid, row, col)
    if grid[row, col] and (num_neighbours == 2 or num_neighbours == 3):
        return True
    if (not grid[row, col]) and num_neighbours == 3:
        return True
    return False


def step(grid):
    new_grid = np.zeros_like(grid, dtype=bool)
    for row in range(0, grid.shape[0]):
        for col in range(0, grid.shape[1]):
            new_grid[row, col] = is_alive(grid, row, col)
    return new_grid


def print_grid(grid):
    grid = np.where(grid, ' X ', ' O ')
    for row in range(0, grid.shape[0]):
        display = ""
        for col in range(0, grid.shape[1]):
            display += grid[row, col]
        print(display)
    print('\n\n')


def play(max_steps=100):
    seed = np.array([[0, 1, 1, 1],
                     [1, 1, 1, 0]], dtype=bool)

    grid = start_game(seed)
    print_grid(grid)
    while np.any(grid) and max_steps > 0:
        grid = step(grid)
        print_grid(grid)
        max_steps -= 1


if __name__ == '__main__':
    play()
