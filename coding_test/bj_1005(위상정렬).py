from collections import defaultdict, deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    work = list(map(int, input().split()))
    building = []
    for _ in range(k):
        building.append(tuple(map(int, input().split())))
    end = int(input())

    dp = [0] * (n+1)
    indegree = [0 for _ in range(n+1)]
    graph = defaultdict(list)
    q = deque()

    for a, b in building:
        graph[a].append(b)
        indegree[b] += 1

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)  
            dp[i] = work[i-1]  

    while q:
        cur = q.popleft()
        for i in graph[cur]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[cur] + work[i-1])
            if indegree[i] == 0:
                q.append(i)
    print(dp[end])