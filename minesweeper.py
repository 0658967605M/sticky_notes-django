# '''Create a function that takes a grid of # and -,
#  where each hash (#) represents a mine and 
# each dash (-) represents a mine-free spot.'''

def minesweeper(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    result = [['-' for _ in range(cols)] for _ in range(rows)]

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#':
                result[r][c] = '#'
            else:
                mine_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '#':
                        mine_count += 1
                result[r][c] = str(mine_count)

    return [''.join(row) for row in result]
print(minesweeper(["---", 
                   "-#-",
                   "---"]))