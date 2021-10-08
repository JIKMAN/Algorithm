from math import ceil
from collections import deque

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    q = deque(progresses)

    cnt = 0
    work = ceil((100 - q[0]) / speeds[0])
    answer = []
    while q:
        idx, now = q.popleft()
        tmp = ceil((100 - now) / speeds[idx])
        if tmp > work:
            answer.append(cnt)
            work = tmp
            cnt = 1
        else:
            cnt += 1
        if not q:
            answer.append(cnt)

    return answer

print(solution(progresses, speeds))