T = 10
for k in range(T):
    n = int(input())
    building = list(map(int, input().split()))


    answer = 0
    for i in range(2, n-2):
        left, right = max(building[i-1], building[i-2]), max(building[i+1], building[i+2])
        sight = min(building[i]-left, building[i]-right)
        if sight > 0:
            answer += sight
        

    print(f'#{k+1} {answer}')

T = int(input())
for t in range(1, T+1):
    n = int(input())
    product = list(map(int, input().split()))
    last = product[-1]
    answer = 0
    for i in range(len(product)-1, -1, -1):
        if last > product[i]:
            answer += last - product[i]
        else:
            last = product[i]
    print(f'#{t} {answer}')