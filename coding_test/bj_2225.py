'''
문제
0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.

덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.

입력
첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.

출력
첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.
'''

import sys
input= lambda : sys.stdin.readline().strip()

n,k=map(int,input().split())

dp=[[0]*201 for i in range(201)]

for i in range(201):
    dp[1][i]=1
    dp[2][i]=i+1

for i in range(2,201):
    dp[i][1]=i
    for j in range(2,201):
        dp[i][j]=(dp[i][j-1]+dp[i-1][j] )% 1000000000

print(dp[k][n])