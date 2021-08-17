numbers = [1, 1, 1, 1, 1]
target = 3

# 주어진 숫자를 모두 사용, '+', '-'를 적절히 조합해서 target 숫자를 만들 수 있는 방법의 수
# BFS 풀이

from collections import deque

def solution(numbers, target):
    answer = 0

    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0])
    queue.append([-numbers[0], 0])

    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

print(solution(numbers, target))

# itertools 라이브러리를 이용

from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

print(solution(numbers, target))

# 문제 2
# 컴퓨터 간의 연결을 나타내는 배열을 보고
# 컴퓨터간 연결되어 있으면 같은 네트워크라고 할 때,
# 네트워크의 개수를 구하는 함수

n = 3 # 컴퓨터의 개수
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] # 컴퓨터간 연결

def solution(n, computers):
    answer = 0
    need = [] # 방문이 필요한 노드를 임시 저장할 배열
    visited = [0] * n # 방문 가능한 모든 노드를 초기화 하여 배열에 저장

    while 0 in visited: # 아직 방문하지 않은 노드가 있다면
        need.append(visited.index(0)) # 그 노드의 인덱스를 방문 할 배열에 할당

        while need: # 방문할 노드를 돌면서
            idx = need.pop(0) # 그 노드의 인덱스
            visited[idx] = 1 # 방문한 상태 '1' 로 표기
            for i in range(n): # 방문한 적이 없으면서, 현재 노드와 연결되어 있는 상태이면
                if visited[i] == 0 and computers[idx][i] == 1:
                    need.append(i) # 다음번 방문할 노드에 추가
        answer += 1 # 더이상 연결된 노드가 없다면 해당 네트워크를 1개의 덩어리로 묶어줌
    return answer

print(solution(n, computers))
