## 해시테이블(Hash Table), 해시충돌 해결방법(Chaining, Open Addressing)

값을 key-value 쌍의 배열로 저장하게 되면 낭비하는 공간이 많이 생길 수 있다.

예시로, 크기가 100인 배열에 2개의 값만 저장하게 된다면 98의 공간이 낭비된다.

 

해시 함수를 이용하면 이를 어느정도 해결할 수 있다.

해시함수는 key를 index로 사용하지 않고 수식에 의해 return된 값을 사용한다.

---

> ### 해시테이블(Hash Table)

해시 테이블은 (Key, Value)로 데이터를 저장하는 자료구조 중 하나로 빠르게 데이터를 검색할 수 있는 자료구조이다. 해시 테이블이 빠른 검색속도를 제공하는 이유는 내부적으로 배열을 사용하여 데이터를 저장하기 때문이다. 해시 테이블은 각각의 Key값에 해시함수를 적용해 배열의 고유한 index를 생성하고, 이 index를 활용해 값을 저장하거나 검색하게 된다. 여기서 실제 값이 저장되는 장소를 버킷 또는 슬롯이라고 한다.

이러한 구조로 데이터를 저장하면 Key값으로 데이터를 찾을 때 해시 함수를 1번만 수행하면 되므로 매우 빠르게 데이터를 저장/삭제/조회할 수 있다. 해시테이블의 평균 시간복잡도는 O(1)이다.

```python
# 파이썬으로 해시 함수 구현

# 방법1
def hash_function(key, array_size, a):
    """key를 0 ~ array_size 범위의 자연수로 바꿔주는 함수"""
    temp = a * key # a와 key를 곱한다
    temp = temp - int(temp) # a와 key를 곱한 값의 소숫점만 저장한다
    
    return int(array_size * temp) # 0 ~ 배열 크기 사이의 자연수로 리턴된다        

print(hash_function(40, 30, 0.3512))  # ---> 1
print(hash_function(110, 30, 0.3512))   # ---> 18

# 방법2
def _hash_function(self, key):
    """
    주어진 key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드
    주의: key는 파이썬 불변 타입이여야 한다.
    """
    return hash(key) % self._capacity
```

---

> ### 해시 충돌

해시함수가 중복되는 경우

---

> ### 체이닝(Chaining)

해시 충돌이 일어나는 경우,

인덱스에 링크드 리스트를 저장하여

중복된 key를 갖는 노드를 연속적으로 저장하는 개념

<br>

\# 체이닝에서 사용하는 링크드 리스트 구현

```python
import LinkedList # 이전의 정의한 더블리 링크드 리스트 함수 이용

class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, key, value): # 기존 더블리 리스트의 data 대신 key와 value
        self.key = key
        self.value = value
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 가장 앞 노드
        self.tail = None  # 가장 뒤 노드
        
    def find_node_with_key(self, key):
    """해당 key를 갖는 노드를 리턴"""
    iterator = self.head

    while iterator is not None:
        if iterator.key == key:
            return iterator
        iterator = iterator.next

    return None
    
    def append(self, key, value):
    """추가 연산 메소드"""
    new_node = Node(key, value)

    # 빈 링크드 리스트일 경우
    if self.head is None:
       self.head = new_node
       self.tail = new_node
    # 이미 노드가 있는 경우
    else:
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        
    def __str__(self):
    """링크드 리스트를 문자열로 표현하는 메소드"""
    res_str = ""

    iterator = self.head

    while iterator is not None:
        # 각 노드의 데이터를 리턴하는 문자열에 더해준다
        res_str += f"{iterator.key}: {iterator.value}\n"
        iterator = iterator.next

    return res_str
    
    --------------# 리턴값 예시
    101: 홍길동
    203: 손흥민
    304: 은가누
```

__\# 체이닝을 쓰는 해시테이블 구현__

```python

class HashTable:
    def __init__(self, capacity):
        self._capacity = capacity  # 파이썬 리스트 크기
        self._table = [LinkedList() for _ in range(self._capacity)]  # 리스트 인덱스에 링크드 리스트 저장

    def _hash_function(self, key):
        # key에 나누기 방법을 사용해서 해시된 값을 리턴하는 메소드
        return hash(key) % self._capacity


    def _get_linked_list_for_key(self, key):
        """주어진 key에 대응하는 인덱스에 저장된 링크드 리스트를 리턴하는 메소드"""
        hashed_index = self._hash_function(key)

        return self._table[hashed_index]


    def _look_up_node(self, key):
        """해당 key를 갖고 있는 노드를 리턴하는 메소드"""
        linked_list = self._get_linked_list_for_key(key)
        return linked_list.find_node_with_key(key)


    def look_up_value(self, key):
        """
        주어진 key에 해당하는 데이터를 리턴하는 메소드
        """
        return self._look_up_node(key).value


    def insert(self, key, value):
        """
        새로운 key - value 쌍을 삽입시켜주는 메소드
        이미 해당 key에 저장된 데이터가 있으면 해당 key에 해당하는 데이터를 바꿔준다
        """
        existing_node = self._look_up_node(key)  # 이미 저장된 key인지 확인한다

        if existing_node is not None:
            existing_node.value = value  # 이미 저장된 key면 데이터만 바꿔주고
        else:
            # 없는 key면 링크드 리스트에 새롭게 삽입시켜준다
            linked_list = self._get_linked_list_for_key(key)
            linked_list.append(key, value)

    def delete_by_key(self, key):
        """주어진 key에 해당하는 key - value 쌍을 삭제하는 메소드"""
        node_to_delete = self._look_up_node(key)
        
        if node_to_delete is not None:
            self._get_linked_list_for_key(key).delete(node_to_delete)

    def __str__(self):
        """해시 테이블 문자열 메소드"""
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]
```



> 체이닝을 쓰는 해시테이블의 평균 시간복잡도

| 연산         | 시간복잡도                        |
| ------------ | --------------------------------- |
| 탐색(search) | O(n), 평균O(1)                    |
| 저장(save)   | 접근+탐색+저장O(1+n+1), 평균 O(1) |
| 삭제(delete) | 접근+탐색+삭제O(1+n+1), 평균 O(1) |

---



> ## Open Addressing

해시충돌을 해결하는 또 다른 방법으로,

인덱스가 이미 존재할 경우 비어있는 인덱스를 찾아 값을 저장하는 방법

* __선형탐사(linear probing)__

충돌이 일어났을 때, 한 칸씩 선형적으로 이동하며 인덱스가 비었는 지 확인하고,

인덱스가 비어있다면 데이터를 삽입함

* __제곱탑사(quadratic probing)__

충돌이 일어났을 때, 한 칸씩 이동하는 것이 아니라, 제곱수 만큼 건너뛰면서 인덱스가 비었는지 확인

배열이 크고 데이터가 많이 저장되어있을 경우, 

선형탐사에 비해 인덱스가 몰려서 저장되는 것을 방지하고, 빠르게 비어있는 인덱스를 찾을 수 있음

**Open Addressing 시간복잡도 (최대의 경우)**

| 삽입 | O(n) |
| ---- | ---- |
| 탐색 | O(n) |
| 삭제 | O(n) |

세 연산 모두 탐사가 포함되기 때문에 최대 O(n)의 시간이 걸린다.

 

단, 체이닝의 경우와 마찬가지로 배열의 크기를 m, 해시 테이블에 들어있는 데이터 쌍 수를 n 이라고 할 때

a = n/m 이라고 할 때 (a는 항상 1보다 작다. )

평균적으로 탐사를 해야 되는 횟수(기댓값)는 1/1-a보다 작다고 할 수 있다.

 

예를들어, 배열이 총 100칸일 때 90개의 key-value 쌍이 저장되었다고 하면,

a = 0.9, 기댓값은 10 즉, 10개 이하의 인덱스를 통해 탐색이 가능하다는 뜻이다.

 

정리해보면,

최악의 경우 인덱스를 찾는데 O(n)의 시간이 걸리지만, 평균적으로 O(1)의 시간이 걸린다고 볼 수 있다.

 

체이닝과 마찬가지로 굉장히 효율적이다.