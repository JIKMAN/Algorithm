# 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
# H-Index를 return 하도록 solution 함수
# H-Index : H번 이상 인용된 논문이 H편 이상일 때  H의 최댓값


def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

# 다른 풀이
'''
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
'''

citations = [3, 0, 6, 1, 5]

print(solution(citations))