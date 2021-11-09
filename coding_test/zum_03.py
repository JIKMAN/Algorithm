import heapq
import copy


def solution(data):

    time = 0
    h = []
    q = []
    tmp = 0
    result = []

    while len(result) < len(data):
        for d in data:
            if time == d[1]:
                heapq.heappush(h, (d[2],d[0]))

        if time == tmp:
            if q:
                page = q.pop()
                result.append(page[1])

        if h:
            if len(q) == 0:
                cur = heapq.heappop(h)
                tmp = copy.deepcopy(time) + cur[0]
                q.append(cur)
         
        time += 1

    return result



data = [[1, 0, 5],[2, 2, 2],[3, 3, 2],[4, 4, 2],[5, 8, 1]]
# 번호, 요청시간, 걸리는 시간

print(solution(data))