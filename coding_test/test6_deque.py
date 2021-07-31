'''현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 
내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 
location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 
몇 번째로 인쇄되는지 return 하도록 solution 함수'''


# solution 1
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
            
# solution 2
from collections import deque

def solution(priorities, location):
    answer = 0
    # 각각의 (index, prioritiies)를 리스트로 저장한 deque를 생성
    deq = deque([(i, p) for i, p in enumerate(priorities)])
    
    while True:
        current = deq.popleft() # que의 첫번째 항목 current 보다
        
        if deq and current[1] < max([d[1] for d in deq]): # 중요도가 큰 수가 있으면 뒤로 보내기
            deq.append(current)
        else: # current 가장 중요도가 크고 현재 항목의 index가 찾는 location과 일치하면 return
            answer += 1
            if current[0] == location:
                return answer 