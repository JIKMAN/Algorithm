'''
문제
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.
'''
# 계속 왜 안되나 싶었는데,, pypy로 제출했더니 통과..

from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline

def bfs(s):
    visited = [False] * (N+1)
    visited[s] = True
    q = deque()
    q.append(s)
    tmp = 0
    while q:
        cur = q.popleft()
        visited[cur] = True
        for v in graph[cur]:
            if visited[v] == False:
                q.append(v)
                tmp += 1
                visited[v] = True
    return tmp

N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split())
    graph[y].append(x)

result = []

for i in range(1, N+1):
    result.append(bfs(i))
    
for idx, k in enumerate(result):
    if k == max(result):
        print(idx+1, end=' ')