'''
문제
통제 할 수 없는 미친 로봇이 평면위에 있다. 그리고 이 로봇은 N번의 행동을 취할 것이다.

각 행동에서 로봇은 4개의 방향 중에 하나를 임의로 선택한다. 그리고 그 방향으로 한 칸 이동한다.

로봇이 같은 곳을 한 번보다 많이 이동하지 않을 때, 로봇의 이동 경로가 단순하다고 한다. (로봇이 시작하는 위치가 처음 방문한 곳이다.) 로봇의 이동 경로가 단순할 확률을 구하는 프로그램을 작성하시오. 예를 들어, EENE와 ENW는 단순하지만, ENWS와 WWWWSNE는 단순하지 않다. (E는 동, W는 서, N은 북, S는 남)

입력
첫째 줄에 N, 동쪽으로 이동할 확률, 서쪽으로 이동할 확률, 남쪽으로 이동할 확률, 북쪽으로 이동할 확률이 주어진다. N은 14보다 작거나 같은 자연수이고,  모든 확률은 100보다 작거나 같은 자연수 또는 0이다. 그리고, 동서남북으로 이동할 확률을 모두 더하면 100이다.

확률의 단위는 %이다.

출력
첫째 줄에 로봇의 이동 경로가 단순할 확률을 출력한다. 절대/상대 오차는 10-9 까지 허용한다.
'''

p = list(map(int, input().split()))
N = p.pop(0)

percent = [p[0]/100, p[1]/100, p[2]/100, p[3]/100]

graph = [[0 for _ in range(N*2 + 1)] for _ in range(N*2 + 1)]
graph[N][N] == 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

total = 0

def dfs(x, y, P, count):
    global total
    if count == N:
        total += P
        return
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if graph[nx][ny] == 1:
            continue
        else:
            dfs(nx, ny, P*percent[i], count+1)
            graph[nx][ny] = 0

dfs(N, N, 1, 0)

print(total)