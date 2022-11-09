n, m = map(int, input().split())

grid = []
for i in range(n):
    grid.append(list(map(int, input())))

# print(grid)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]


def dfs(grid, x, y, visited):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if visited[nx][ny] == False and grid[nx][ny] == 0:
                # visited[nx][ny] = True
                dfs(grid, nx, ny, visited)


answer = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0 and visited[i][j] == False:
            dfs(grid, i, j, visited)
            answer += 1

print(answer)

'''
[INPUT]
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

[OUTPUT]
8
'''