N, r, c = map(int, input().split())

def check(N, r, c):
    v = (2 ** N) / 2
    if r < v and c < v:
        return 0
    elif r < v and c >= v:
        c -= v
        return int((2 ** N) * (2 ** N) / 4)
    elif r >= v and c < v:
        r -= v
        return int((2 ** N) * (2 ** N) / 2)
    elif r >= v and c >= v:
        r -= v
        c -= v
        return int((2 ** N) * (2 ** N) / 4 * 3)

arr = [[0, 1], [2, 3]]
result = 0
while N > 0:
    if N <= 1:
        result += arr[r][c]
        N -= 1
        break
    else:        
        result += check(N, r, c)
        v = int((2 ** N) / 2)
        if r < v and c >= v:
            c -= v
        elif r >= v and c < v:
            r -= v
        elif r >= v and c >= v:
            r -= v
            c -= v
        N -= 1

print(result)