'''현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와
내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때,
내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.
중요도 순서대로 인쇄해야 함'''

from collections import deque

test1 = [2, 1, 3, 2]
test_l1 = 2

test2 = [1, 1, 9, 1, 1, 1]
test_l2 = 0

def solution(priorities, location):
    count = 0

    que = deque([[p, i] for i, p in enumerate(priorities)])

    while que:
        poped = que.popleft()
        if poped[0] < max(q[0] for q in que):
            que.append(poped)
        else:
            count += 1
            if poped[1] == location:
                return count

print(solution(test1, test_l1))
print(solution(test2, test_l2))