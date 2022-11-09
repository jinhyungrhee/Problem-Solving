from collections import deque

n, m = map(int, input().split())

grid = []
for i in range(n):
    grid.append(list(map(int, input())))

# print(grid)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * m for _ in range(n)]

q = deque([(0, 0)])
visited[0][0] = 1

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if visited[nx][ny] == 0 and grid[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

# print(visited)
print(visited[n - 1][m - 1])


'''
[INPUT]
5 6
101010
111111
000001
111111
111111

[OUTPU]
10
'''