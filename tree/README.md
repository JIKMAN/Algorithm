## 트리

* 계층적 관계가 있는 데이터를 자료로 정리해 놓은 구조
* 트리를 이용하여 정렬, 데이터 압축 등 다양한 문제를 해결할 수 있다.

* 딕셔너리, 세트, 큐 등 다양한 추상 자료형을 구현하는데 쓰일 수 있다.





### 이진트리 구조

![이진트리구조](https://gmlwjd9405.github.io/images/data-structure-tree/tree-terms.png)

###  **완전 이진 트리(Complete Binary Tree)**

완전 이진 트리는 이진트리 구조로 되어 있는 것은 당연한 속성이며 Leaf 노드를 제외한 모든 부모 노드가 자식 노드를 2개씩 가지고 있는 것을 완전 이진트리구조라고 한다.

![완전이진트리](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbzhstp%2FbtqCZyflXWX%2FcBXGK7DIPKE1KHhZABrWY1%2Fimg.png)

> #### 완전 이진 트리에서 탐색

![완전이진트리탐색](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbbMb1l%2Fbtq8pj6wraX%2FYkWjiOZQkH45hBCU1uk3X0%2Fimg.png)

* 부모 노드의 인덱스 x2 = 자식 노드의 인덱스

  ex) 12(3번 인덱스)의 자식 노드는 10(6번 인덱스)

 

* 자식 노드의 인덱스 / 2 의 정수부분 = 부모 노드의 인덱스

  ex) 14(7번 인덱스)의 부모 노드는 7 / 2 = 3.5 (정수부분 3) 즉, 12(3번인덱스)

```python
# 완전이진트리의 탐색 구현

def get_parent_index(complete_binary_tree, index):
    """index번째 노드의 부모 노드의 인덱스를 리턴하는 함수"""
    parent_index = index // 2
    
    if 0 < parent_index < len(complete_binary_tree): # 인덱스가 배열에 포함되는 경우에만 리턴
        return parent_index
        
    return None


def get_left_child_index(complete_binary_tree, index):
    """index번째 노드의 왼쪽 자식 노드의 인덱스를 리턴하는 함수"""
    left_child_index = 2 * index

    if 0 < left_child_index < len(complete_binary_tree): # 인덱스가 배열에 포함되는 경우에만 리턴
        return left_child_index

    return None
    

def get_right_child_index(complete_binary_tree, index):
    """index번째 노드의 오른쪽 자식 노드의 인덱스를 리턴하는 함수"""
    right_child_index = 2 * index + 1

    if 0 < right_child_index < len(complete_binary_tree): # 인덱스가 배열에 포함되는 경우에만 리턴
        return right_child_index

    return None
```

### 트리 순회

트리 구조에서 트리 순회를 통해 데이터를 탐색할 수 있다.

트리 순회를 통해 트리 내의 모든 데이터에 접근할 수 있다.(트리의 모든 데이터에 3을 더하라 등..)

트리 순회에는 대표적으로 3가지 방법이 있는데

- pre-order : **현재 노드를 출력** 후 재귀적으로 왼쪽 자식 노드, 오른쪽 자식 노드 순서로 탐색
- post-order : 재귀적으로 왼쪽 자식 노드 탐색 후 **현재 노드를 출력** 후 오른쪽 자식 노드를 탐색
- in-order : 재귀적으로 왼쪽 자식 노드, 오른쪽 자식 노드 순서로 탐색 후 **현재 노드를 출력**



```python
#이진 트리 구조가 존재한다고 가정함

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def pre_order(node):
    """pre-order 순회 함수"""
    if node is not None:
        print(node.data)
        pre_order(node.left_child)
        pre_order(node.right_child)
        
pre_order(root_node)     

>>>  F B A D C E G I H 


def in_order(node):
    """in-order 순회 함수"""
    if node is not None:
        in_order(node.left_child)
        print(node.data)
        in_order(node.right_child)
        
in_order(root_node)

>>>  A B C D E F G H I


def post_order(node):
    """post-order 순회 함수"""
    if node is not None:
        post_order(node.left_child)
        post_order(node.right_child)
        print(node.data)
        
post_order(root_node)
        
>>>  A C E D B H I G F
```













## **힙(Heap)**

힙은 완전 이진트리이고, 자식 노드들이 특정한 성질을 가지고 정렬되어 있는 구조이다. 부모 노드가 자식 노드들보다 크다면 최대 힙(Max Heap)구조라고 하고, 부모 노드가 자식 노드들보다 작다면 최소 힙(Min Heap)구조라고 한다.