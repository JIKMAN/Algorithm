# kakao 2021 인턴쉽 4. 미로탈출

'''
그림의 원은 방을 나타내며 원 안의 숫자는 방 번호를 나타냅니다.
방이 n개일 때, 방 번호는 1부터 n까지 사용됩니다.
화살표에 표시된 숫자는 방과 방 사이를 이동할 때 걸리는 시간을 나타냅니다.
화살표가 가리키고 있는 방향으로만 이동이 가능합니다. 즉, 위 그림에서 2번 방에서 1번 방으로는 이동할 수 없습니다.
그림에 표시된 빨간색 방인 2번 방은 함정입니다.
함정 방으로 이동하는 순간, 이동한 함정 방과 연결되어 있는 모든 길의 방향이 반대가 됩니다.
위 그림 1번 방에서 2번 방으로 이동하는 순간 1에서 2로 이동할 수 있던 길은 2에서 1로 이동할 수 있는 길로 바뀌고, 3에서 2로 이동할 수 있던 길은 2에서 3으로 이동할 수 있는 길로 바뀝니다.
똑같은 함정 방을 두 번째 방문하게 되면 원래 방향의 길로 돌아옵니다. 즉, 여러 번 방문하여 계속 길의 방향을 반대로 뒤집을 수 있습니다.
미로를 탈출하는데 필요한 최단 시간은 다음과 같습니다.
1→2: 2번 방으로 이동합니다. 이동 시간은 2입니다.
함정 발동: 2번 방과 연결된 모든 길의 방향이 반대가 됩니다.
2→3: 3번 방으로 이동합니다. 이동 시간은 3입니다.
탈출에 성공했습니다. 총 이동시간은 5입니다.
방의 개수를 나타내는 정수 n, 출발 방의 번호 start, 도착 방의 번호 end, 통로와 이동시간을 나타내는 2차원 정수 배열 roads, 함정 방의 번호를 담은 정수 배열 traps이 매개변수로 주어질 때, 미로를 탈출하는데 필요한 최단 시간을 return 하도록 solution 함수를 완성해 주세요.

1 ≤ n ≤ 1,000
1 ≤ start ≤ n
1 ≤ end ≤ n
1 ≤ roads의 행 길이 ≤ 3,000
roads의 행은 [P, Q, S]로 이루어져 있습니다.
P에서 Q로 갈 수 있는 길이 있으며, 길을 따라 이동하는데 S만큼 시간이 걸립니다.
1 ≤ P ≤ n
1 ≤ Q ≤ n
P ≠ Q
1 ≤ S ≤ 3,000
서로 다른 두 방 사이에 여러 개의 길이 존재할 수도 있습니다.
0 ≤ traps의 길이 ≤ 10
1 ≤ traps의 원소 ≤ n
시작 방과 도착 방은 함정이 아닙니다.
항상 미로를 탈출할 수 있는 경우만 주어집니다.
'''

n, start, end = 4, 1, 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

array = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for r in roads:
    array[r[0]][r[1]] = r[2]



def trap(x, nodes):
    for i in nodes[x]:
        nodes[i[0]].append((x, i[1]))
        nodes[x].remove(i)
    for k in nodes.keys():
        for v in nodes[k]:
            if v[0] == x:
                if (k, v[1]) not in nodes[x]:
                    nodes[x].append((k, v[1])) 
                    nodes[k].remove(v)



# 연결노드, 거리 dic 생성
nodes = {}
for i in range(1,n+1):
    nodes[i] = []
for r in roads:
    nodes[r[0]].append((r[1], r[2]))

print(nodes)
trap(2,nodes)
print(nodes)