'''
각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders,
"스카피"가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때,
"스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
'''

## 내 풀이

from itertools import combinations

books = {}
result = []
answer = []

def solution(orders, course):
    for i in range(len(orders)):
        new = sorted(list(orders[i]))
        
        for c in course:
            result = list(combinations(new, c))
            
            for r in result:
                joined = "".join(r)
                
                if joined not in books:
                    books[joined] = 1
                else:
                    books[joined] += 1
    tmp_book = Counter(books)

    # for c in course:
    #     tmp_book = {}
    #     for book in books:
    #         if len(book) == c:
    #             tmp_book[book] = books[book]

    for tmp in tmp_book:
        if tmp_book[tmp] == max(tmp_book.values()) and tmp_book[tmp] > 1:
            answer.append(tmp)
    answer.sort()
    return answer


order01 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course01 = [2,3,4]

print(solution(order01, course01))


## Counter 함수를 이용하면 더 쉽다고 한다.

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)

    # 와..