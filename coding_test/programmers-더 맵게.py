# 더 맵게
'''
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.
섞은 음식 = 가장 안매운 음식 + (2번째로 안매운 음식 * 2)
'''

# 처음에 결과는 맞았으나 효율성 테스트 실패
scoville = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
    count = 0
    scoville.sort()

    for i in range(len(scoville) - 1):
        scoville[0] = scoville[0] + (scoville[1] * 2)
        count += 1
        scoville.sort()
        scoville.pop(0)

        if scoville[0] >= K:
            return count
    return -1


print(solution(scoville, K))


# 힙을 이용하여 재도전

import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    
    
    while scoville[0] < K:
        
        most = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        mix = most + second * 2

        heapq.heappush(scoville, mix)   

        count += 1

        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return count

print(solution(scoville, K))
