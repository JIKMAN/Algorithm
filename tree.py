### 이진트리의 기본 구조 ###

## 함수
class TreeNode(): # 트리 노드 클래스
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


## 전역




## Main
node1 = TreeNode('화사')
node2 = TreeNode('솔라')
node1.left = node2
node3 = TreeNode('문별')
node1.right = node3
node4 = TreeNode('휘인')
node2.left = node4
node5 = TreeNode('쯔위')
node2.right = node5
node6 =TreeNode('선미')
node3.left = node6

print(node1.data)
print(node1.left.data, node1.right.data)
print(node1.left.left.data, node1.left.right.data, node1.right.left.data)