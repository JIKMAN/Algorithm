'''
주사위는 위와 같이 생겼다. 주사위의 여섯 면에는 수가 쓰여 있다. 위의 전개도를 수가 밖으로 나오게 접는다.

A, B, C, D, E, F에 쓰여 있는 수가 주어진다.

지민이는 현재 동일한 주사위를 N3개 가지고 있다. 이 주사위를 적절히 회전시키고 쌓아서, N×N×N크기의 정육면체를 만들려고 한다. 이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.

N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. 둘째 줄에 주사위에 쓰여 있는 수가 주어진다. 위의 그림에서 A, B, C, D, E, F에 쓰여 있는 수가 차례대로 주어진다. N은 1,000,000보다 작거나 같은 자연수이고, 쓰여 있는 수는 50보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.
'''

n = int(input())
num = list(map(int, input().split()))

if n == 1:
    print(sum(num) - max(num))
else:
    numlist = []
    numlist.append(min(num[0], num[5]))
    numlist.append(min(num[1], num[4]))
    numlist.append(min(num[2], num[3]))

    numlist.sort()

    num1 = numlist[0]
    num2 = num1 + numlist[1]
    num3 = num2 + numlist[2]

    result = 0
    n1 = (n - 2) * (n - 2) + (n - 1) * (n - 2) * 4
    n2 = 4 * (n - 2) + 4 * (n - 1)
    n3 = 4

    result += n1 * num1
    result += n2 * num2
    result += n3 * num3

    print(result)

