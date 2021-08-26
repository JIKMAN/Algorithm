'''frequently used Standard Library'''

# sum()
result = sum([1,2,3,4,5])
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)

#eval()
result = eval("(3+5)*7")

#sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x:x[1], reverse=True)

# 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것 ( nPr )
from itertools import permutations
data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)

# 조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것 ( nCr )
from itertools import combinations
result = list(combinations(data, 2))
print(result)

# 중복 순열
from itertools import product

result = list(product(data, repeat=2))
print(result)

#중복 조합
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data, 2))
print(result)

# Counter : 등장 횟수를 세는 기능,
# 리스트 같은 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는 지 알려줌
from collections import Counter

count_list = Counter(['red', 'blue', 'red', 'green', 'blue', 'orange', 'blue'])

print(count_list['blue'])
print(count_list['green'])
print(dict(count_list)) # 사전 자료형으로 반환

# 최대 공약수
import math

a = 21
b = 14

print(math.gcd(a, b))

# 최소 공배수(LCM)을 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

print(lcm(a, b))

# 플로이드 워셔 알고리즘(완전탐색)

INF = 200 * 100000 + 1

def floyd(dist, n):
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

# 배열 회전

key = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

print(list(zip(*key[::-1])))

print(*key[::-1])


# 정규식 치환
import re

id = 'A-B_?C=;D'

id = re.sub('[\W_]', '.', id)
print(id)