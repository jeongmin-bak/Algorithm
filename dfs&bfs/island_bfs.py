from collections import deque

def island_bfs_queue(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue

            cnt += 1
            queue = deque([(row, col)])
            while queue:
                x, y = queue.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= rows or nx < 0 or ny >= cols or ny < 0 or grid[nx][ny] != '1':
                        continue
                    grid[nx][ny] = '0'
                    queue.append([nx, ny])
    return cnt

print(island_bfs_queue(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
