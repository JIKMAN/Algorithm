# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 
# 얼마가 모자라는지를 return 하도록 solution 함수

def solution(price, money, count):
    result = 0
    for i in range(1, count+1):
        result += price * i
    if result > money:
        return (result - money)
    else:
        return 0

# 다른 풀이
'''
def solution(price, money, count):
    return max(sum([price * i for i in range(1, count+1)]) - money, 0)
'''

price = 3
money = 20
count = 4
print(solution(price, money, count))