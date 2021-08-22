# 섬의 개수

'''
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
'''


n = 4
m = 5
island = [[1, 0, 1, 0, 0],
          [1, 0, 0, 0, 0],
          [1, 0, 1, 0, 1],
          [1, 0, 0, 1, 0]]



dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if island[x][y] == 0:
        return False
    if island[x][y] == 1:
        island[x][y] = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            dfs(nx, ny)
        return True

def solution(n, m, island):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                cnt += 1
    return cnt

print(solution(n,m,island))

n = 5
m = 5
island = [[1, 0, 1, 0, 1],
          [0, 0, 0, 0, 0],
          [1, 0, 1, 0, 1],
          [0, 0, 0, 0, 0],
          [1, 0, 1, 0, 1]]

print(solution(n,m,island))