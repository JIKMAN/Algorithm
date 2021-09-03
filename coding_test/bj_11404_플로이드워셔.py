'''
n개의 도시, m개의 버스 route = [i번째 도시에서, j번 도시로 가는데, k만큼 걸린다.]
i에서 j로 가기위한 최소 루트를 구하시오. (i != j)
갈수 없는 경우 0
'''

n = 5 # 도시의 개수
m = 14 # 버스의 개수
route = [[1, 2, 2],
[1, 3, 3],
[1, 4, 1],
[1, 5, 10],
[2, 4, 2],
[3, 4, 1],
[3, 5, 1],
[4, 5, 3],
[3, 5, 10],
[3, 1, 8],
[1, 4, 2],
[5, 1, 7],
[3, 4, 2],
[5, 2, 4]]

distance = [[100 for _ in range(n+1)] for _ in range(n+1)]
for i in range(len(distance)):
    distance[i][i] = 0

for r in route:
    if distance[r[0]][r[1]] > r[2] or distance[r[0]][r[1]] == 0:
        distance[r[0]][r[1]] = r[2]


def floyd(distance, n):
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

floyd(distance, n)
for dis in distance:
    print(dis)