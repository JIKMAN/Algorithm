# greedy algorythm

# 거스름 돈 문제

n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n = n % coin

print(count)

# 문제 1
# 주어진 수 n에서 k로 나누거나 1을 빼거나
# 두가지 연산을 이용해 1을 만드는 횟수의 최소값

# 방법 1 ( 시간복잡도 O(N))
n = 25
k = 4
cnt = 0
while n > 1:
    if n % k == 0:
        n = n / k
        cnt += 1
    else:
        n -= 1
        cnt += 1
print(cnt)

# 방법 2 ( 시간복잡도 O(logN) )
n = 25
k = 4
result = 0
while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k
result += (n - 1)
print(result)

# 문제 2
# + 와 x 연산만을 이용해 주어진 각자리 숫자의 연산을 가장 큰 값으로 만들기

num1 = "02984"
num2 = "576"

def solution(num):
    result = int(num[0])
    for i in range(1, len(num)):
        if result == 0 or int(num[i]) == 0:
            result += int(num[i])
        else:
            result *= int(num[i])
    return result


print(solution(num1)) 
print(solution(num2)) 


# 문제 3
# 모험가 길드
# 각 모험가는 공포도를 가지고 있고 공포도 만큼의 인원이 한 그룹이 되어야 함
# 모험을 떠나지 않아도 됌
# 이때 떠날 수 있는 그룹의 수의 최댓값

group = [2, 3, 1, 2, 2]

def solution2(group):
    group.sort()
    result = 0 # 총 그룹의 수
    count = 0 # 현재 그룹에 포함된 모험가 수

    for i in group:
        count += 1
        if count >= i:
            result += 1
            count = 0
    return result
print(solution2(group))