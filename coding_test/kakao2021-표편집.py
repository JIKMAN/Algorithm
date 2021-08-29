# https://programmers.co.kr/learn/courses/30/lessons/81303

# 처음 표의 행 개수 n (5 ~ 1000000)
# 처음 선택된 행의 위치 k ( 0 <= k < n)
# 문자열 배열 cmd ( 1 ~ 200000)


## 실패한 풀이

def move(array, cur):
    if cur == len(array) - 1:
        while array[cur - 1] == 'X':
            cur = cur - 1
        cur = cur - 1
        return cur
    while array[cur + 1] == 'X':
        cur = cur + 1
    cur = cur + 1
    return cur

def up(array, cur, x):
    if cur <= x:
        return 0
    for i in range(x):
        while array[cur - 1]  == 'X':
            if cur <= x-i:
                return 0
            cur = cur - 1
        cur = cur - 1
    return cur

def down(array, cur, x):
    if cur >= len(array) - 1 - x:
        return len(array) - 1
    for i in range(x):
        while array[cur + 1] == 'X':
            if cur >= len(array) - i -x:
                return len(array) - 1
            cur = cur + 1
        cur = cur + 1
    return cur



def solution(n, k, cmd):
    array = ['O' for _ in range(n)]
    cur = k
    removed = []

    for c in cmd:
        c = c.split(" ")
        
        if c[0] == 'D':
            cur = down(array, cur, int(c[1]))
        
        if c[0] == 'U':
            cur = up(array, cur, int(c[1]))
        
        if c[0] == 'C':
            removed.append(cur)
            array[cur] = "X"
            cur = move(array, cur)
        
        if c[0] == 'Z':
            idx = removed.pop()
            array[idx] = 'O'
        

    return "".join(array)


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

print(solution(n, k, cmd))

'''
OOOOOOOO
OOOOXOOO
OOOOXOOO
OXOOXOOO
OXOOXOOO
OXOXXOOO
OXOXXOOO
OXOXOOOO
OOOXOOOO
'''
    

# removed = deque()

## 다른 풀이

from collections import defaultdict


def solution(n, k, cmd):
    answer = ["O" for i in range(n)]
    linked_list = defaultdict(list)

    for i in range(1, n + 1):
        linked_list[i].append(i - 1)
        linked_list[i].append(i + 1)

    stack = []
    k += 1

    for instruction in cmd:
        if instruction[0] == "D":
            for _ in range(int(instruction[2:])):
                k = linked_list[k][1]

        elif instruction[0] == "U":
            for _ in range(int(instruction[2:])):
                k = linked_list[k][0]
                
        elif instruction[0] == "C":
            prev, next = linked_list[k]
            stack.append([prev, next, k])
            answer[k - 1] = "X"

            if next == n + 1:
                k = linked_list[k][0]
            else:
                k = linked_list[k][1]

            if prev == 0:
                linked_list[next][0] = prev
            elif next == n + 1:
                linked_list[prev][1] = next
            else:
                linked_list[prev][1] = next
                linked_list[next][0] = prev

        elif instruction[0] == "Z":
            prev, next, now = stack.pop()
            answer[now - 1] = "O"

            if prev == 0:
                linked_list[next][0] = now
            elif next == n + 1:
                linked_list[prev][1] = now
            else:
                linked_list[prev][1] = now
                linked_list[next][0] = now

    return "".join(answer)

print(solution(n, k, cmd))