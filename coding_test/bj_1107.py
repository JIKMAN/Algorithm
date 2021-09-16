'''
문제
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오. 

수빈이가 지금 보고 있는 채널은 100번이다.

입력
첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.  둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.

출력
첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.
'''

# 처음 풀이 = 답은 나오지만 효율이 안나옴

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
broken = list(map(int, input().split()))

if N == 100:
    print(0)

arr = []

def same(num, arr):
    for i in arr:
        if str(i) in str(num):
            return True
    return False

def minus(num, arr):
    tmp = num
    while same(num, arr) == True:
        num -= 1
    return len(str(num)) + tmp - num

def plus(num, arr):
    tmp = num
    while same(num, arr) == True:
        num += 1
    return len(str(num)) + num - tmp

arr.append(minus(N, broken))
arr.append(plus(N, broken))
        
print(min(arr))

# 다른 코드를 참고한 새로운 코드

n = int(input())

m = int(input())
if m != 0:
    arr = list(map(int, input().split()))
else:
    arr = []
num = 100

ans = abs(n - 100)
for i in range(1000001):
    numArr = list(str(i))
    flag = False
    # 숫자를 누를 수 있는 지 검사
    for k in numArr:
        if int(k) in arr:
            flag = True
            break

    if flag:
        continue
    # 해당 숫자를 누를 수 있다면 n까지 가는 방법 + 숫자를 누른횟수를 구해서 비교한다.
    else:
        ans = min(ans, abs(n - i) + len(str(i)))

print(ans)