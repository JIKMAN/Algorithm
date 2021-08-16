# Dynamic Programming
# 이미 해결한 문제는 동적 할당하여 미리 저장해 놓고, 다시 해결할 필요 없도록 함


# 1피보나치 수열

d = [0] * 100

# top-down

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))

# bottom-up

d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])

'''----------------------------------------------------------------'''

# 2
# 인접하지 않은 숫자들의 합 중 가장 큰 합은?

sum_list = [1, 3, 5, 1, 2, 1, 1, 3, 6, 2, 1, 2]
sum_list2 = [1, 3, 5, 4, 2]

def solution(sum_list):
    # 계산을 저장할 배열 생성
    d[0] * len(sum_list)
    
    d[0] = sum_list[0]
    d[1] = sum_list[1]

    for i in range(2, len(sum_list)):
        d[i] = max(d[i - 1], d[i - 2] + sum_list[i])
    
    return d[i]

print(solution(sum_list))
print(solution(sum_list2))

'''----------------------------------------------------------------'''

# 3
# 정수 X 가 주어졌을때,
# X가 5로 나누어 떨어지면 5로 나누고,
# 3으로 나누어 떨어지면 3으로 나누고,
# 2로 나누어지면 2로 나누고
# 나누어지지 않으면 1을 빼준다.
# 4가지 연산을 적절히 사용해 X를 1로 만들 수 있는 연산 횟수의 최소값


def solution3(num):
    d= [0] * (num + 1)

    # d[1] = 0 : 1은 연산 횟수 0

    for i in range(2, num + 1):
        d[i] = d[i - 1] + 1

        if i % 2 == 0:
            d[i] = min(d[i // 2] + 1, d[i])
        elif i % 3 == 0:
            d[i] = min(d[i // 3] + 1, d[i])
        elif i % 5 == 0:
            d[i] = min(d[i // 5] + 1, d[i])
                    
    return d[num]

X = 18
print(solution3(X))
X = 23
print(solution3(X))