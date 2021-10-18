import copy
from collections import deque

M, N = map(int, input().split())
island =[]
for _ in range(M):
    island.append(list(input().strip()))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# def dfs(x, y):

def bfs(i, j):
    q = deque()
    q.append((i, j))
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and visit[nx][ny] == 0 and island[nx][ny] != 'W':
                visit[nx][ny] = 1
                island[nx][ny] = island[x][y] + 1
                cnt = max(cnt, island[nx][ny])
                q.append((nx,ny))
    return cnt

result = 0
for i in range(M):
    for j in range(N):
        if island[i][j] != "W":
            visit = [[0] * N for _ in range(M)]
            island[i][j] = 0
            visit[i][j] = 1
            result = max(result, bfs(i,j))

print(result)




