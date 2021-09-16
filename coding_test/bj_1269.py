from collections import defaultdict
from collections import deque

N, M, s = map(int, input().split())
nodes = []
for _ in range(M):
    nodes.append(list(map(int, input().split())))

graph = defaultdict(list)

for node in nodes:
    graph[node[0]].append(node[1])
    graph[node[1]].append(node[0])

def bfs(s):
    q = deque()
    q.append(s)
    visited = [False] * (N+1)
    visited[s] = True
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for i in range(1, N+1):
            if visited[i] == False and i in graph[cur]:
                q.append(i)
                visited[i] = True


visited = [False] * (N+1)
visited[s] = True
def dfs(s):
    print(s, end=' ')
    for i in range(1, N+1):
        if visited[i] == False and i in graph[s]:
            visited[i] = True
            dfs(i)

dfs(s)
print()            
bfs(s)