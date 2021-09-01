# programmers - 디스크 컨트롤러

'''
각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

제한 사항
jobs의 길이는 1 이상 500 이하입니다.
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.
'''

# 해결방법
'''
1. 현재 시간에서 수행 가능한 job을 필터링 한다.

2. 필터링한 작업들 중 소요 시간이 가장 짧은 job을 먼저 수행한다.

    작업 완료 후 (소요 시간) + (현재 시간) - (요청시간)을 answer에 더한다.

3. 만약 수행 가능한 작업이 없다면 현재 시간을 +1 해준다.

4. 모든 작업들이 완료되면 answer을 job의 갯수로 나눈다.
'''

import heapq
 
def solution(jobs):
    answer = 0
    jobsLength = len(jobs)
    currentTime = 0
    i = 0
    requestedJobs = []
    heapq.heapify(requestedJobs)
    jobs = sorted(jobs)
 
    
    
    while jobsLength > i : 
 
        for x in jobs[:]:
            if x[0]<=currentTime:
                heapq.heappush(requestedJobs, [x[1], x[0]])
                jobs.pop(0)
            else:
                break
        
        if len(requestedJobs) > 0 :
            currentJob = heapq.heappop(requestedJobs)
            currentTime += currentJob[0]
            answer += (currentTime - currentJob[1])
            i += 1
            
        else:
            currentTime += 1
    
    return int(answer / jobsLength)