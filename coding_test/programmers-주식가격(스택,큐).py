# 주식가격(스택,큐)
'''
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
'''
from collections import deque


prices = [1, 2, 3, 2, 3]

def solution(prices):
    queue = deque(prices)

    answer = []

    while queue:
        tmp = queue.popleft()
        
        cnt = 0
        for q in queue:
            cnt += 1
            if tmp > q:
                break
        answer.append(cnt)
    return answer

print(solution(prices))