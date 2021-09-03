# 정점 개수 V  (1≤ V ≤20,000) 
# 간선 개수 E  (1≤ E ≤300,000)
'''
모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 
시작 정점의 번호 K(1≤K≤V)가 주어진다. 
각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력
'''
V, E = 5, 6
route = [[5, 1, 1], [1, 2, 2], [1, 3, 3], [2, 3, 4], [2, 4, 5], [3, 4, 6]]

def solution(V, E, route, end):
    graph = {}
    for r in route:
        if r[0] not in graph:
            graph[r[0]] = [(r[1], r[2])]
        else:
            graph[r[0]].append((r[1], r[2]))

    distance = [11] * (V+1)
    distance[1] = 0


    need = [1]
    while need:
        cur = need.pop()
        if cur in graph:
            for v in graph[cur]:
                need.append(v[0])
                distance[v[0]] = min(distance[v[0]], distance[cur]+v[1])
    
    if distance[end] == 11:
        return 'INF'

    return distance[end]

print(solution(V, E, route, 4))