import sys
input = sys.stdin.readline

input = list(map(int, input().split()))
r1 = (input[0], input[2])
r2 = (input[1], input[3])

s = max(abs(r1[0]), r1[1], abs(r2[0]), r2[1])

graph = [[0 for _ in range(s * 2 + 1)] for _ in range(s * 2 + 1)]

row = [0, -1, 0, 1]
col = [1, 0, -1, 0]

count = 1
rep = 1
tmp = 0
x, y = s, s
while count <= len(graph) * len(graph):
    for _ in range(2):
        for _ in range(rep):
            count += 1
            if count >= len(graph) * len(graph):
                break
            graph[x + row[tmp % 4]][y + col[tmp % 4]] = str(count)
            x, y = x + row[tmp % 4], y + col[tmp % 4]
        tmp += 1

    rep += 1    
graph[s][s] = '1'
graph[2*s][2*s] = str(len(graph) * len(graph))


result = []
for i in range(r2[0]+s, r2[1] + s + 1):
    tmp = []
    for j in range(r1[0]+s, r1[1] + s + 1):
        tmp.append(graph[j][i])
    
    mx = 0
    for t in tmp:
        mx = max(mx, len(t))
    
    for i in range(len(tmp)):
        if len(tmp[i]) < mx:
            tmp[i] = ' ' * (mx - len(tmp[i])) + tmp[i]
    result.append(tmp)

for i in range(len(result[0])):
    for j in range(len(result)):
        print(result[j][i], end = " ")
    print()
