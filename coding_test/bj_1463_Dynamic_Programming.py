# dinamic programming

'''
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 
연산을 사용하는 횟수의 최솟값
'''

case = int(input())

dp = [0,0,1,1] # [0, case가 1일 때 경우의 수, 2일 때, 3일 때 ...]

# dp[n]의 최솟값은 n의 이전 단계의 최솟값 + 1
# 이전 단계의 경우의 수는 3가지
# dp[n] = min(dp[n-1] , dp[n//2], dp[n//3) + 1
for i in range(4, case+1):
    dp.append(dp[i-1]+1) # 2나 3으로 나눠지지 않는 경우 이전 단계 + 1
    if i%2 == 0: # 2로 나눠질 경우
        dp[i] = min(dp[i//2]+1, dp[i])
    if i%3 == 0: # 3으로 나눠질 경우
        dp[i] = min(dp[i//3]+1, dp[i])

print(dp[case])
