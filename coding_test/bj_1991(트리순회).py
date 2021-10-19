'''
입력
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
'''

n = int(input())
nodes = []
for _ in range(n):
    nodes.append(list(input().split()))

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

tree = {}

for node in nodes:
    tree[node[0]] = Node(node[0], node[1], node[2])

root = 'A'

def pre_order(node):
    tmp = tree[node]
    print(tmp.data, end ="")
    if tmp.left != '.':
        pre_order(tmp.left)
    if tmp.right != '.':
        pre_order(tmp.right)

def in_order(node):
    tmp = tree[node]
    if tmp.left != '.':
        in_order(tmp.left)
    print(tmp.data, end ="")
    if tmp.right != '.':
        in_order(tmp.right)

def post_order(node):
    tmp = tree[node]
    if tmp.left != '.':
        post_order(tmp.left)
    if tmp.right != '.':
        post_order(tmp.right)
    print(tmp.data, end ="")


pre_order(root)
print()
in_order(root)
print()
post_order(root)