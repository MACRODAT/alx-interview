#!/usr/bin/python3
"""Defines island perimeter finding function."""
def inGrid(_w, _h, i, j):
    """Check if (x, y) is within the grid bounds."""
    return (i >= 0 and j >= 0 and i < _w and j < _h)


def neighboors(i, j, _w, _h):
    """Yield neighboring cell coordinates (excluding the center cell)."""
    combinations = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
    for x, y in combinations:
        if inGrid(_w, _h, x, y):
            yield (x, y)


def countWater(_w, _h, i, j, grid):
    """Count the number of water cells surrounding a given land cell."""
    per = 0
    combinations = [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1)]
    for x, y in combinations:
        if inGrid(_w, _h, x, y):
            if grid[y][x] == 0:
                per += 1
        else:
            per += 1
    return per


def island_perimeter(grid):
    """Calculate the perimeter of the island in the grid."""
    # let's do 1
    # @param grid the grid
    isIsland = False
    _h = len(grid)
    _w = len(grid[0])
    for j in range(0, len(grid)):
        for i in range(len(grid[0])):
            isIsland = False
            if grid[j][i] == 0:
                continue
            for x, y in neighboors(i, j, _w, _h):
                if x != y and not isIsland:
                    if grid[y][x] == 0:
                        isIsland = True
            if not isIsland:
                # let's do 2
                grid[j][i] = -1
    # Now, let's do 3
    perimeter = 0
    for j in range(0, len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == 1:
                perimeter += countWater(_w, _h, i, j, grid)
    return perimeter



def island_perimeter2(grid):
    """Return the perimiter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edges += 1
    return size * 4 - edges * 2


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    print(island_perimeter2(grid))
