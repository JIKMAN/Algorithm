'''
문제
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
'''


from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

N, E = map(int, input().split())

route = []

for i in range(E):
    route.append(list(map(int, input().split())))

v1, v2 = map(int, input().split())

graph = defaultdict(list)
for r in route:
    graph[r[0]].append((r[2], r[1]))
    graph[r[1]].append((r[2], r[0]))

INF = sys.maxsize

def dijkstra(start):
    distance = [INF] * (N+1)
    distance[start] = 0

    h = [(0, start)]
    while h:
        dist, cur = heapq.heappop(h)
        if dist > distance[cur]:
            continue

        for node in graph[cur]:
            cost = dist + node[0]

            if cost < distance[node[1]]:
                distance[node[1]] = cost
                heapq.heappush(h, (cost, node[1]))

    return distance


r1 = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[N]
r2 = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[N]

result = min(r1, r2)
print(result if result < INF else -1)

