from typing import List

def dfs(grid, x, y):
    grid[x][y] = 0   # directly use grid to record visited points.
    if x > 0 and grid[x - 1][y] == "1":
        dfs(grid, x - 1, y)

    if x < len(grid) - 1 and grid[x + 1][y] == "1":
        dfs(grid, x + 1, y)

    if y > 0 and grid[x][y - 1] == "1":
        dfs(grid, x, y - 1)

    if y < len(grid[0]) - 1 and grid[x][y + 1] == "1":
        dfs(grid, x, y + 1)


def numIslands(grid: List[List[str]]) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += 1
                dfs(grid, i, j)
    return count

