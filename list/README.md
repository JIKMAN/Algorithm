## 링크드 리스트

### 싱글리 링크드 리스트(Single Linked List)

* 배열과는 다르게 크기를 유연하게 바꿀 수 있는 자료구조

* 노드 (Node) 들의 연결된 리스트로 구성이 되며 노드는 데이터와 다음 노드를 가르키는 포인터(링크)로 구성

![singlenode](https://t1.daumcdn.net/cfile/tistory/225E1A455891519012)

파이썬으로 싱글리 링크드 리스트를 구현

```python
class Node:
    """노드 클래스"""
    def __init__(self, data):
        self.data = data  # 노드의 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스
        
        
class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 맨 처음 노드
        self.tail = None  # 맨 뒤 노드
```

구현한 링크드 리스트 클래스의 다양한 매소드 구현

```python
		def find_node_with_data(self, data):
            """탐색 메소드"""
            iterator = self.head

            while iterator is not None:
                if iterator.data == data:
                    return iterator

                    iterator = iterator.next
            return None
            
        def find_node(self, index):
            """인덱스를 통한 접근"""
            iterator = self.head

            for _ in range(index):
                iterator = iterator.next

            return iterator

        def append(self, data):
            """데이터 추가 메소드"""
            new_node = Node(data)

            # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드
            if self.head is None:
               self.head = new_node
               self.tail = new_node
            # 링크드 리스트가 비어 있지 않으면
            else:
                self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
                self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다
                
        def insert_after(self, prev_node, data):
            """주어진 노드 뒤 삽입 메소드"""
            new_node = Node(data)

            #가장 마지막에 삽입
            if prev_node is self.tail:
                self.tail.next = new_node
                self.tail = new_node
            else: # 두 노드 사이에 삽입
                new_node.next = prev_node.next
                prev_node.next = new_node
        
        def prepend(self, data):
        	"""링크드 리스트의 가장 앞에 데이터 삽입"""
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
        
        def delete_after(self, prev_node):
            """주어진 노드 뒤의 노드를 삭제"""
            if prev_node.next is self.tail:
                prev_node.next = None
                self.tail = prev_node
            else:
                prev_node.next = prev_node.next.next
        
        def pop_left(self):
        	"""가장 앞 노드 삭제 메소드"""
            data = self.head.data

            if self.head is self.tail:
                self.tail = None
                self.head = None
            else:
                self.head = self.head.next

            return data
        

        def __str__(self):
            """링크드  리스트를 문자열로 표현"""
            res_str = "|"

            # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
            iterator = self.head

            # 링크드  리스트 끝까지 돈다
            while iterator is not None:
                # 각 노드의 데이터를 리턴하는 문자열에 더해준다
                res_str += f" {iterator.data} |"
                iterator = iterator.next # 다음 노드로 넘어간다

            return res_str
```

* 링크드 리스트의 시간 복잡도

| 접근                                | O(n)                |
| ----------------------------------- | ------------------- |
| 탐색                                | O(n)                |
| 삽입                                | O(1)                |
| 삭제                                | O(1)                |
| 가장 앞 또는 뒤에 접근 후 삽입/삭제 | O(1)                |
| 원하는 노드 접근 후 삽입/삭제       | O(n+1)<br /> = O(n) |

---

### 더블리 링크드 리스트

![더블리링크드리스트](https://t1.daumcdn.net/cfile/tistory/26139E3F589594521C)

파이썬으로 더블리 링크드 리스트를 구현



```python
class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스
        
        
class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 가장 앞 노드
        self.tail = None  # 가장 뒤 노드

        
    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정한다"""

        iterator = self.head # 링크드 리스트를 돌기 위해 필요한 노드 변수

        # index 번째 있는 노드로 간다
        for _ in range(index):
            iterator = iterator.next

        return iterator
    
    def insert_after(self, previous_node, data):
        """추가 연산 메소드"""
        new_node = Node(data)
        
        if previous_node is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            new_node.prev = previous_node
            new_node.next = previous_node.next
            
            previous_node.next.prev = new_node
            previous_node.next = new_node
    
    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
            
        else:
            # 링크드 리스트 가장 앞 데이터 삭제할 때
            if node_to_delete is self.head:
                self.head = node_to_delete.next
                self.head.prev = None
            # 링크드 리스트 가장 뒤 데이터 삭제할 떄
            elif node_to_delete is self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            # 두 노드 사이에 있는 데이터 삭제할 때
            else:
                node_to_delete.prev.next = node_to_delete.next
                node_to_delete.next.prev = node_to_delete.prev
                
        return node_to_delete.data

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str
```

---

> ### __싱글리 링크드 리스트 vs 더블리 링크드 리스트__

가장 뒤에 접근 + 이전 노드를 삭제 하는 경우의 시간 복잡도

싱글리 O(n+1)

더블리 O(1+1)

 

__\# 싱글리 링크드 리스트는 앞에 있는 노드에 바로 접근할 수 없다.__

__\# 더블리 링크드 리스트의 경우 레퍼런스를 저장하는 추가적 공간을 더 많이 차지한다.__