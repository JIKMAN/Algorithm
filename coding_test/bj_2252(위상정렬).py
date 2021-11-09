from collections import defaultdict, deque

n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(tuple(map(int, input().split())))

indegree = [0] * (n + 1)
q = deque()
graph = defaultdict(list)



for a, b in arr:
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
    
while q:
    cur = q.popleft()
    for x in graph[cur]:
        indegree[x] -= 1
        if indegree[x] == 0:
            q.append(x)

    print(cur, end = ' ')