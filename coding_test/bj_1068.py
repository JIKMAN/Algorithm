'''
입력
첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

출력
첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.
'''
import sys
input = sys.stdin.readline


def dfs(del_node, nodes):
    nodes[del_node] = -2
    for i in range(len(nodes)):
        if nodes[i] == del_node:
            dfs(i, nodes)

N =  int(input())
nodes = list(map(int, input().split()))
del_node = int(input())

dfs(del_node, nodes)
count = 0
for i in range(len(nodes)):
    if nodes[i] != -2 and i not in nodes:
        count += 1
print(count)