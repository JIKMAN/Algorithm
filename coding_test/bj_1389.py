# bj_1389_케빈 베이컨의 6단계 법칙
# 플로이드-와샬

n, m = map(int, input().split())

relation = []

for i in range(m):
    relation.append(tuple(map(int, input().split())))

from collections import defaultdict

graph = [[5001 for _ in range(n+1)] for _ in range(n+1)]

for a, b in relation:
    graph[a][b], graph[b][a] = 1, 1

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

result = []
for i in range(1, n+1):
    result.append(sum(graph[i]))

print(result.index(min(result))+1)