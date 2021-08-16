# Dynamic Programming
# 이미 해결한 문제는 동적 할당하여 미리 저장해 놓고, 다시 해결할 필요 없도록 함
# 피보나치 수열

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