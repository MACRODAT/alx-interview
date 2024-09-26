#!/usr/bin/python3
""" Calculations:
# my approach is simple:
# 1. identify the squares surrounding the water
# 2. remove the rest inland.
# 3. calculate the adjacency of each to water
"""


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


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
