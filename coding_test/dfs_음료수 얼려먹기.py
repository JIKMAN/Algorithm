## 음료수 얼려먹기

'''
N * M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0 이고 칸막이가 존재하는 부분은 1이다. 
즉, 0으로 연결된 부분이 얼음 한 덩이가 얼려져 나오는 것이다. 
구멍이 뚫려 있는 부분 끼리 상, 하, 좌, 우로 붙어 있는 경우가 서로 연결된 경우가 된다. 
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
'''

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 1:
        return False
    else:
        graph[x][y] = 1
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)
        return True

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1
print(cnt)