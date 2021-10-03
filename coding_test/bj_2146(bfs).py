import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs1(i, j):
    global count
    q = deque()
    q.append([i, j])
    vis[i][j] = True
    arr[i][j] = count

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and not vis[nx][ny]:
                vis[nx][ny] = True
                arr[nx][ny] = count
                q.append([nx, ny])

def bfs2(z):
    global answer
    dist = [[-1] * n for _ in range(n)] 
    q = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == z:
                q.append([i, j])
                dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] > 0 and arr[nx][ny] != z:
                answer = min(answer, dist[x][y])
                return
            if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
vis = [[False] * n for _ in range(n)]
count = 1
answer = sys.maxsize

for i in range(n):
    for j in range(n):
        if not vis[i][j] and arr[i][j] == 1:
            bfs1(i, j)
            count += 1

for i in range(1, count):
    bfs2(i)

print(answer)