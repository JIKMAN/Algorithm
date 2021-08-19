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

    for c in course:
        tmp_book = {}
        for book in books:
            if len(book) == c:
                tmp_book[book] = books[book]

        for tmp in tmp_book:
            if tmp_book[tmp] == max(tmp_book.values()) and tmp_book[tmp] > 1:
                answer.append(tmp)
    answer.sort()
    return answer

order01 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course01 = [2,3,4]
print(solution(order01, course01))