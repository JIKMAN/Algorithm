* [트리](#트리)
  * [이진탐색트리](#이진-탐색-트리)
  * [완전이진트리](#완전-이진-트리(complete-binary-tree))

* [힙](#힙의-조건)
  * [우선순위 큐](#우선순위-큐)

* [그래프](#그래프)
* [BFS, DFS](#그래프-탐색)
  
* [최단경로 알고리즘](#최단경로-알고리즘)



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

-----------------------------------

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

트리 순회를 통해 트리 내의 모든 데이터에 접근할 수 있다. (트리의 모든 데이터에 3을 더하라 등..)

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

---



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

* 힙은 대표적으로 __정렬 알고리즘__ , __우선순위 큐__ 라는 추상 자료형을 구현하는데 사용된다.
* 우선 힙의 정렬을 구현해보자

> #### 힙 정렬

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



> #### 우선순위 큐

* 힙에 데이터를 삽입
* 힙 속성을 유지하도록 삽입한 데이터를 조정
* 첫번째 루트 노드는 항상 가장 큰(우선순위가 높은) 노드임

```python
def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2  # 삽입된 노드의 부모 노드의 인덱스 계산
    if 0 < parent_index < len(tree) and tree[index] > tree[parent_index]:
          tree[index], tree[parent_index] = tree[parent_index], tree[index]  # 부모 노드와 삽입된 노드의 위치 교환
          reverse_heapify(tree, parent_index)  # 바뀐 부모 노드에서 다시 reverse_heapify 호출

class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙


    def insert(self, data):
        """삽입 메소드"""
        self.heap.append(data)
        reverse_heapify(self.heap, len(self.heap)-1)


    def __str__(self):
        return str(self.heap)


# 실행 코드
priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
priority_queue.insert(3)
priority_queue.insert(10)
priority_queue.insert(11)
priority_queue.insert(13)

print(priority_queue)

---------------------------------

>>> [None, 13, 9, 11, 3, 6, 1, 10]
```



> #### 우선순위 큐에서 우순순위 데이터 추출

* 루트 노드와 마지막 노드를 바꾼다.
* 마지막 노드(가장 큰 수)를 변수에 저장
* root 노드에 heapify 함수를 호출하여 힙 속성 부여
* 변수에 저장한 데이터를 추출

```python
import heapify
import reverse_heapify

class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙

'''현재 우선순위 큐를 전에 만든 [None, 13, 9, 11, 3, 6, 1, 10] 라고 가정'''
    def extract_max(self):
        """최고 우선순위 데이터 추출 메소드"""
        len(self.heap) - 1 = last_node_idx
        
        self.heap[1], self.heap[last_node_idx] = \
        self.heap[last_node_idx], self.heap[1]# root 노드와 마지막 노드의 위치 바꿈
        
        max_value = self.heap.pop()  # 힙에서 마지막 노드 추출(삭제)해서 변수에 저장
        
        heapify(self.heap, 1, len(self.heap))  # 새로운 root 노드를 대상으로 heapify 호출해서 힙 속성 유지
        return max_value  # 최우선순위 데이터 리턴
```

> #### 시간 복잡도

* 힙의 삽입 : 노드 삽입 `O(1)` + 그 노드를 힙으로 만드는 과정 최대 `O(log(n))` = 총 `O(lg(n))`

* 힙의 추출 : root노드와 마지막 노드 위치바꿈 `O(1)` + 마지막 노드 변수에 저장(pop) `O(1)`

  ​					+ 새로운 root에 힙속성 부여 `O(lg(n))` + 변수 리턴 `O(1)` = 총 `O(lg(n))`

|                           |         데이터 삽입          | 데이터 추출  |
| :-----------------------: | :--------------------------: | :----------: |
|     정렬된 동적 배열      | *O*(lg(*n*)) - 이진탐색 이용 |     O(1)     |
| 정렬된 더블 링크드 리스트 |             O(n)             |     O(1)     |
|            힙             |         *O*(lg(*n*))         | *O*(lg(*n*)) |

* 삽입에는 힙이 효율적
* 추출에는 링크드 리스트 또는 동적 배열이 효율적

---

# 그래프

>  ## 그래프 (Graph) 란?

- 그래프는 실제 세계의 현상이나 사물을 정점(Vertex) 또는 노드(Node) 와 간선(Edge)로 표현하기 위해 사용

#### 관련 용어

- 노드 (Node): 위치를 말함, 정점(Vertex)라고도 함
- 간선 (Edge): 위치 간의 관계를 표시한 선으로 노드를 연결한 선이라고 보면 됨 (link 또는 branch 라고도 함)
- 인접 정점 (Adjacent Vertex) : 간선으로 직접 연결된 정점(또는 노드)

### 그래프 (Graph) 종류

#### 무방향 그래프 (Undirected Graph)

- 방향이 없는 그래프

- 간선을 통해, 노드는 양방향으로 갈 수 있음

- 보통 노드 A, B가 연결되어 있을 경우, (A, B) 또는 (B, A) 로 표기

  	<img src="https://www.fun-coding.org/00_Images/undirectedgraph.png" alt="img" style="zoom:33%;" />

#### 방향 그래프 (Directed Graph)

- 간선에 방향이 있는 그래프
- 보통 노드 A, B가 A -> B 로 가는 간선으로 연결되어 있을 경우, <A, B> 로 표기 (<B, A> 는 B -> A 로 가는 간선이 있는 경우이므로 <A, B> 와 다름) 

<img src="https://www.fun-coding.org/00_Images/directedgraph.png" alt="img" style="zoom:33%;" />





#### 가중치 그래프 (Weighted Graph) 또는 네트워크 (Network)

- 간선에 비용 또는 가중치가 할당된 그래프

  <img src="https://www.fun-coding.org/00_Images/weightedgraph.png" alt="img" style="zoom:33%;" />

  

> ### 그래프와 트리의 차이

|                |                       그래프                       |                     트리                      |
| :------------: | :------------------------------------------------: | :-------------------------------------------: |
|      정의      | 노드와 노드를 연결하는 간선으로 표현되는 자료 구조 | 그래프의 한 종류, 방향성이 있는 비순환 그래프 |
|     방향성     |       방향 그래프, 무방향 그래프 둘다 존재함       |             방향 그래프만 존재함              |
|     사이클     |  사이클 가능함, 순환 및 비순환 그래프 모두 존재함  |    비순환 그래프로 사이클이 존재하지 않음     |
|   루트 노드    |              루트 노드 존재하지 않음               |               루트 노드 존재함                |
| 부모/자식 관계 |           부모 자식 개념이 존재하지 않음           |            부모 자식 관계가 존재함            |

---

> ### 파이썬으로 그래프를 표현

```python
# 인접 그래프 예시

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(graph)

---------------------

{'A': ['B', 'C'],
 'B': ['A', 'D'],
 'C': ['A', 'G', 'H', 'I'],
 'D': ['B', 'E', 'F'],
 'E': ['D'],
 'F': ['D'],
 'G': ['C'],
 'H': ['C'],
 'I': ['C', 'J'],
 'J': ['I']}
```

```python
# 인접 행렬 예시

class Graph():
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

A, B, C, D = 0, 1, 2, 3

G = Graph(4) # 4x4 2차원 배열의 그래프
G.graph[A][B] = 1
G.graph[A][C] = 1
G.graph[A][D] = 1
G.graph[B][A] = 1
G.graph[B][C] = 1
G.graph[C][D] = 1
G.graph[C][A] = 1
G.graph[C][B] = 1
G.graph[D][A] = 1
G.graph[D][C] = 1


for i in range(4):
    for j in range(4):
        print(G.graph[i][j], end=' ')
    print()
    
-----------------------------

>>> 0 1 1 1 
    1 0 1 0
    1 1 0 1
    1 0 1 0
```

> ### 인접 리스트 vs 인접 행렬

* 노드의 개수 : V (Vertex)
* 엣지의 개수 : E (Edge)

노드 수가 V 일 때, 그래프 안에는 최대 V^2 개의 Edge가 들어갈 수 있다.

#### 차지하는 공간

인접행렬은 V x V의 행렬이므로 V^2의 공간을 차지

인접리스트는 노드를 저장하는 공간 V + 노드마다 포함된 엣지를 저장하는 공간 E, 총 V+E

#### 연결됐는지 확인하는데 걸리는 시간

인접 행렬은 두 노드가 인접했는지 아닌지 O(1)로 확인 (`matrix[3][5]` 같은 방식)

인접 리스트는 한 노드의 리스트 안에 특정 역이 저장됐는지를 탐색하므로, 최소 O(1) 최대 O(V)

#### 한 노드에 연결된 모든 시간을 확인

인접 행렬은 그 노드의 배열(혹은 행)을 전부 살펴야 하므로 O(V)

인접 리스트는 인접 노드의 래퍼런스를 가지고 있으므로 최소 O(1), 최대(모든 노드와 연결되있는 경우) O(V)

|                     | 인접행렬 | 인접리스트 |
| ------------------- | -------- | ---------- |
| 차지하는 공간       | O(V^2)   | O(V+E)     |
| 연결 확인           | O(1)     | O(1)~O(V)  |
| 연결 노드 전체 탐색 | O(V)     | O(1)~O(V)  |

대체로 인접 리스트를 사용하는 것이  좀 더 효율적이다.

---



> ### 그래프 탐색

###  BFS 와 DFS 란?

대표적인 그래프 탐색 알고리즘

* 너비 우선 탐색 (Breadth First Search) : 정점들과 같은 레벨에 있는 노드들 (형제 노드들)을 먼저 탐색하는 방식

* 깊이 우선 탐색 (Depth First Search) : 정점의 자식들을 먼저 탐색하는 방식



- BFS 방식: A - B - C - D - G - H - I - E - F - J
  - 한 단계씩 내려가면서, 해당 노드와 같은 레벨에 있는 노드들 (형제 노드들)을 먼저 순회함
- DFS 방식: A - B - D - E - F - C - G - H - I - J
  - 한 노드의 자식을 타고 끝까지 순회한 후, 다시 돌아와서 다른 형제들의 자식을 타고 내려가며 순화함

![img](https://www.fun-coding.org/00_Images/BFSDFS.png)

> ### BFS 알고리즘 구현

- 자료구조 큐를 활용함
  - need_visit 큐와 visited 큐, 두 개의 큐를 생성

```python
from collections import deque

def bfs(graph, start_node):
    visited = list()
    need_visit = deque()
    
    need_visit.append(start_node) # 첫 노드를 방문할 큐에 추가
    
    while need_visit:
        current = need_visit.popleft() # 방문할 큐에서 다음 노드를 꺼내옴
        if current not in visited: # 방문한 적이 없으면
            visited.append(current) # 방문한 노드에 추가
            need_visit.extend(graph[current]) # 인접한 노드들을 방문할 큐에 추가
    
    return visited
```

* 시간 복잡도 : O(V + E)

> ### DFS 알고리즘 구현

- 자료구조 스택과 큐를 활용함
  - need_visit 스택과 visited 큐, 두 개의 자료 구조를 생성

```python
def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    
    while need_visit:
        current = need_visit.pop()
        if current not in visited:
            visited.append(current)
            need_visit.extend(graph[current])
    
    return visited
```

* 시간 복잡도 : O(V + E)

---

> ## 최단경로 알고리즘

### BFS Predecessor

* BFS 알고리즘 진행하면서 해당 노드가 어느 노드에서 왔는지를 표시한 것이 Predecessor

* 시작점은 아무데서도 오지 않았으니 None

* Predecessor에서 Backtracking하여 어떤 노드에서 시작점까지의 최단 경로를 추적해 나갈 수 있다.

  

### Dijkstra 최단경로

### 다익스트라 알고리즘 로직

- 첫 정점을 기준으로 연결되어 있는 정점들을 추가해 가며, 최단 거리를 갱신하는 기법

- 다익스트라 알고리즘은 너비우선탐색(BFS)와 유사

  - 첫 정점부터 각 노드간의 거리를 저장하는 배열을 만든 후, 첫 정점의 인접 노드 간의 거리부터 먼저 계산하면서, 첫 정점부터 해당 노드간의 가장 짧은 거리를 해당 배열에 업데이트

- 우선순위 큐를 활용한 다익스트라 알고리즘

  - 우선순위 큐는 MinHeap 방식을 활용해서, 현재 가장 짧은 거리를 가진 노드 정보를 먼저 꺼내게 됨

  1) 첫 정점을 기준으로 배열을 선언하여 첫 정점에서 각 정점까지의 거리를 저장

     * 초기에는 첫 정점의 거리는 0, 나머지는 무한대로 저장함 (inf 라고 표현함)

     * 우선순위 큐에 (첫 정점, 거리 0) 만 먼저 넣음

  2) 우선순위 큐에서 노드를 꺼냄

     * 처음에는 첫 정점만 저장되어 있으므로, 첫 정점이 꺼내짐

     * 첫 정점에 인접한 노드들 각각에 대해, 첫 정점에서 각 노드로 가는 거리와 현재 배열에 저장되어 있는 첫 정점에서 각 정점까지의 거리를 비교한다.

     * 배열에 저장되어 있는 거리보다, 첫 정점에서 해당 노드로 가는 거리가 더 짧을 경우, 배열에 해당 노드의 거리를 업데이트한다.

     * 배열에 해당 노드의 거리가 업데이트된 경우, 우선순위 큐에 넣는다.

       * 결과적으로 너비 우선 탐색 방식과 유사하게, 첫 정점에 인접한 노드들을 순차적으로 방문하게 됨

       * 만약 배열에 기록된 현재까지 발견된 가장 짧은 거리보다, 더 긴 거리(루트)를 가진 (노드, 거리)의 경우에는 해당 노드와 인접한 노드간의 거리 계산을 하지 않음

  3)  2번의 과정을 우선순위 큐에 꺼낼 노드가 없을 때까지 반복한다.

  <img src="https://www.fun-coding.org/00_Images/dijkstra.png" alt="img" style="zoom:33%;" />

- 파이썬의 heapq 라이브러리 활용

```python
import heapq 

queue = []

# heappush input한 데이터를 힙 구조로 만들어 주는 함수
heapq.heappush(queue, [2, 'A'])
heapq.heappush(queue, [5, 'B'])
heapq.heappush(queue, [1, 'C'])
heapq.heappush(queue, [7, 'D'])
print (queue)
for index in range(len(queue)):
    print (heapq.heappop(queue))
-------------------------------
>>>[[1, 'C'], [5, 'B'], [2, 'A'], [7, 'D']]
[1, 'C']
[2, 'A']
[5, 'B']
[7, 'D']
```



```python
import heapq

def dijkstra(graph, start, end):
    # 시작에서 각 정점까지의 거리를 저장할 딕셔너리를 생성하고, 무한대(inf)로 초기화
    distances = {vertex: [float('inf'), None] for vertex in graph}
    '''
    { 첫번째 인덱스 : 최단 거리, 두번째 인덱스 : 경로
    'A' = [inf, None]
    'B' = [inf, None]
    ...
    }
    의 형식으로 저장됨
    '''

    # 그래프의 시작 정점의 거리는 0으로 초기화 해줌
    distances[start] = [0, start]

    # 모든 정점이 저장될 큐를 생성합니다.
    queue = []

    # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start][0], start])
    
    # 현재 큐의 상태 : [[0, 'A']]
    while queue:
        
        # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트
        current_distance, current_vertex = heapq.heappop(queue)
        # 현재 current_distance = 0
        #  	  current_vertex = 'A'
        
        # 더 짧은 경로가 있다면 무시한다.
        if distances[current_vertex][0] < current_distance:
            continue
            
        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 가까울 경우에는
            if distance < distances[adjacent][0]:
                # 거리를 업데이트합니다.
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])
    
    path = end
    path_output = end + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += start
    print (path_output)
    return distances

# 방향 그래프
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(mygraph, 'A', 'F'))

----------------------------------

>>> F->E->D->A
>>> {'A': [0, 'A'], 'B': [6, 'C'], 'C': [1, 'A'], 'D': [2, 'A'], 'E': [5, 'D'], 'F': [6, 	 'E']}
```

