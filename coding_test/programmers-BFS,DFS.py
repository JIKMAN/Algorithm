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
data = [('A', 'B'), ('C', 'D')]

print(list(product(*data)))