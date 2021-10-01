from collections import deque
from collections import defaultdict

n = 8
k = 8
time = [0, 10, 20, 1, 5, 8, 7, 1, 43]
nodes = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (5, 7), (6, 7), (7, 8)]
end = 7
indegree = [0] * (n+1)
dp = [0] * (n+1)

graph = defaultdict(list)

for i in nodes:
    graph[i[0]].append(i[1])
    indegree[i[1]] += 1

q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = time[i]

while q:
    cur = q.popleft()
    for i in graph[cur]:
        indegree[i] -= 1
        dp[i] = max(time[i] + dp[cur], dp[i])
        if indegree[i] == 0:
            q.append(i)
print(dp[end])