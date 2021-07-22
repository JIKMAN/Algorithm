## 트리

* 계층적 관계가 있는 데이터를 자료로 정리해 놓은 구조
* 트리를 이용하여 정렬, 데이터 압축 등 다양한 문제를 해결할 수 있다.

* 딕셔너리, 세트, 큐 등 다양한 추상 자료형을 구현하는데 쓰일 수 있다.

> 트리의 구성요소

- **node** : 트리에서 데이터를 저장하는 기본 요소 (다른 연결 노드에 대한 branch 정보 포함)
- **root node** : 트리 맨 위에 있는 노드
- **level** : 최상위 노드를 level 0으로 하였을 때, 하위 branch로 연결된 노드의 깊이를 나타냄
- **parenet node** : 어떤 노드의 다음 레벨에 연결된 노드
- **child node** : 어떤 노드의 상위 레벨에 연결된 노드
- **leaf node (=terminal node)** : child node가 하나도 없는 노드
- **sibling (brother node)** : 동일한 parent node를 가진 노드
- **depth** : tree에서 node가 가질 수 있는 최대 level



### 이진트리 구조

![이진트리구조](https://media.vlpt.us/images/muchogusto/post/7a926065-c1dd-4d07-9541-b7f386ce0d7c/image.png)

### 이진 탐색 트리

 이진 트리에 다음과 같은 추가적인 조건이 있는 트리

- 왼쪽 노드는 해당 노드보다 작은 값
- 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음
- 왼쪽 노드 < 해당 노드 < 오른쪽 노드
- 주요 용도 : 데이터 **검색(탐색)**
- 장점 : 탐색 **속도**를 개선할 수 있음
  

> #### 선형 탐색 vs 이진 트리 탐색

* __이진 트리 탐색 : 평균 시간 복잡도 O(logn), 최악의경우 O(n)__

![이진탐색트리](https://media.vlpt.us/images/muchogusto/post/98ed4227-b18d-4b6d-8294-a41d8f28abe4/image.png)

### 이진 탐색 트리 구현 및 탐색 구현

```python
## 트리 노드 클래스
class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

## 전역
memory = []
root = None

## 이진트리로 만들 배열
nameArray = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

# 루트 노드 생성
node = TreeNode()
node.data = nameArray[0]
root = node
memory.append(root)


# 이진 탐색 트리 구현
for name in nameArray[1:]:
    node = TreeNode()
    node.data = name
    
    current = root
    while True: # 작은 것은 left, 큰 것은 right로 할당
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left # 왼쪽에 이미 있으면 다시 비교
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right # 오른쪽에 이미 있으면 다시 비교

    memory.append(node)

print('이진 탐색 트리 구성 완료')

## 데이터를 탐색할 때 완전 효율적
# 이진 탐색 트리를 이용한 탐색
findlist = ['마마무', '에스파'] # 찾을 이름
for i in findlist:
    findName = i

    current = root
    count = 0

    while True:
        count +=1
        if current.data == findName:
            print(findName, count,'번 만에 찾았다!')
            break
        elif findName < current.data:
            if current.left == None:
                print(findName, '목록에 없음..')
                break
            current = current.left
        else:
            if current.right == None:
                print('목록에 없음..')
                break
            current = current.right
            
>>> 이진 탐색 트리 구성 완료
>>> 마마무 3 번 만에 찾았다!
>>> 에스파 못찾음..
```

---



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

![트리 순회](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FKvv0T%2Fbtq8sB5E0Sz%2F9INMZKxiBlFKdjawLmhce0%2Fimg.png)

```python
#이진 트리 구조가 존재한다고 가정함

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order(node):
    """pre-order 순회 함수"""
    if node is not None:
        print(node.data)
        pre_order(node.left)
        pre_order(node.right)
        
pre_order(root_node)     

>>>  F B A D C E G I H 


def in_order(node):
    """in-order 순회 함수"""
    if node is not None:
        in_order(node.left)
        print(node.data)
        in_order(node.right)
        
in_order(root_node)

>>>  A B C D E F G H I


def post_order(node):
    """post-order 순회 함수"""
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.data)
        
post_order(root_node)
        
>>>  A C E D B H I G F
```













## **힙(Heap)**

데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)

힙은 완전 이진트리이고, 자식 노드들이 특정한 성질을 가지고 정렬되어 있는 구조이다. 

부모 노드가 자식 노드들보다 크다면 최대 힙(Max Heap)구조라고 하고, 부모 노드가 자식 노드들보다 작다면 최소 힙(Min Heap)구조라고 한다.



> #### 힙의 조건

1. 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다. (최대 힙의 경우)
   * 최소 힙의 경우는 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 작음

2.  완전 이진 트리 형태를 가짐

### 힙과 이진 탐색 트리의 공통점과 차이점

- 공통점: 힙과 이진 탐색 트리는 모두 이진 트리임
- 차이점:
  - 힙은 각 노드의 값이 자식 노드보다 크거나 같음(Max Heap의 경우)
  - 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드, 그 다음 오른쪽 자식 노드 값이 가장 큼
  - 힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽이라는 조건은 없음
    - 힙의 왼쪽 및 오른쪽 자식 노드의 값은 오른쪽이 클 수도 있고, 왼쪽이 클 수도 있음
- 이진 탐색 트리는 탐색을 위한 구조, 힙은 최대/최소값 검색을 위한 구조 중 하나로 이해하면 됨



> #### 힙의 동작

```python
def heapify(tree, index, tree_size): # 주어진 배열(tree)에서
    """배열의 해당 인덱스를 heap으로 만드는 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        tree[index], tree[largest] = tree[largest], tree[index] # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를 대상으로 heap 과정을 거친다
```

* 해당 heapify 동작을 마지막 노드부터 루트 노드까지 수행하면 전체 트리가 힙 조건을 만족한다.

> #### 힙 정렬

```python
def heapsort(tree):
    """힙 정렬 함수"""
    tree_size = len(tree)

    # 마지막 인덱스부터 처음 인덱스까지 heapify를 호출한다 -> 받은 리스트 (tree)를 힙으로 만듦
    for index in range(tree_size, 0, -1):
        heapify(tree, index, tree_size) -> tree는 힙이 된다.

    # 마지막 인덱스부터 처음 인덱스까지
    for i in range(tree_size-1, 0, -1):
        tree[1], tree[i] = tree[i], tree[1]
        heapify(tree, 1, i)
        '''가장 큰 수인 루트노드 tree[1]과 마지막 노드를 교환 하면
        마지막 노드가 가장 큰 수가 됌.
        그 다음 마지막 인덱스를 제외한 나머지 리스트로 같은 과정을 반복하면
        높은 숫자부터 쌓여 오름차순으로 정렬되게 된다.'''
```

---

### 정렬 알고리즘 비교

| 정렬 알고리즘 | 시간 복잡도                |
| ------------- | -------------------------- |
| 선택 정렬     | O(n2)                      |
| 삽입 정렬     | O(n2)                      |
| 합병 정렬     | O(nlg(n))                  |
| 퀵 정렬       | 평균 O(nlg(n)), 최악 O(n2) |
| 힙 정렬       | O(nlg(n))                  |

