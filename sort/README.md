# 알고리즘

- 탐색 알고리즘
  - [선형 탐색](#선형탐색)
  - [이진 탐색](#이진-탐색)
  - [이진 트리 탐색](#이진-트리-탐색)
- 정렬 알고리즘
  - [버블 정렬](#버블-정렬)
  - [삽입 정렬](#삽입-정렬)
  - [선택 정렬](#선택-정렬)
  - [퀵 정렬](#퀵-정렬)
  - [합병 정렬](#합병-정렬)
  - [힙 정렬](#힙-정렬)
  - [계수 정렬(Counting Sort)](#계수-정렬counting-sort)
  - [기수 정렬(Radix Sort)](#기수-정렬radix-sort)
  - [정렬 알고리즘 비교](#정렬-알고리즘-비교)
  - [시간 복잡도 비교](#시간-복잡도-비교)
- [알고리즘 비교 시뮬레이션 사이트](https://www.toptal.com/developers/sorting-algorithms)
- [파이썬 함수의 시간복잡도](#list-operations)



## 탐색 알고리즘

> ### 선형 탐색

리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘

```python
# 선형 탐색
# 해당 element가 list에 존재하면 해당 element의 index를 리턴
def linear_search(element, array):
    for i in range(len(array)):
        if element == array[i]:
            return i
    return None
```



> ### 이진 탐색

이진 탐색 알고리즘은 찾을 값을 중간인덱스를 기준으로 비교해가며 인덱스를 절반씩 줄여가며 탐색한다.

이진 탐색 알고리즘은 선형 탐색 알고리즘과 달리, 정렬된 리스트를 전제로 한다.

```python
# 이진 탐색
# 해당 element가 list에 존재하면 해당 element의 index를 리턴
def binary_search(element, array):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            end = mid -1
        else:
            start = mid + 1
```



> ### 이진 트리 탐색

이진 트리 구조를 이용한 탐색 방법

```python
## 이진 트리 탐색

# 주어진 배열
nameArray = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

# 루트 노드 생성
node = TreeNode()
node.data = Array[0]
root = node


# 이진 탐색 트리 구현 -> 주어진 배열을 이진 탐색을 위한 트리로 만들어주는 함수
for element in Array[1:]:
    node = TreeNode()
    node.data = element
    
    current = root
    while True: # 작은 것은 left, 큰 것은 right로 할당
        if element < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left # 왼쪽에 이미 있으면 다시 비교
        else: # element > corrent.data인 경우
            if current.right == None:
                current.right = node
                break
            current = current.right # 오른쪽에 이미 있으면 다시 비교
            
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
            
----------------------------------
>>> 마마무 3 번 만에 찾았다!
>>> 에스파 목록에 없음..    


```

---

## 정렬 알고리즘

> ### 버블 정렬

두 인접한 데이터를 비교해서, 앞에 있는 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘

![img](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)

```python
# 버블 정렬

def bubble_sort(array):
    for n in range(len(array)):
        for i in range(len(array) - n - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array
```



> ### 삽입 정렬

- 삽입 정렬은 두 번째 인덱스부터 시작
- 해당 인덱스(key 값) 앞에 있는 데이터(B)부터 비교해서 key 값이 더 작으면, B값을 뒤 인덱스로 복사
- 이를 key 값이 더 큰 데이터를 만날때까지 반복, 그리고 큰 데이터를 만난 위치 바로 뒤에 key 값을 이동

<img src="https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif" alt="img" style="zoom:67%;" />

```python
def insertion_sort(array):
    for n in range(len(array)): # array 크기만큼 반복
        data = array[n] # n번째 데이터
        for i in range(n, 0, -1):
            if data < array[i - 1]: # n번째 데이터와 그 이전 데이터들을 차례로 비교
                array[i - 1], array[i] = array[i], array[i - 1]
            else:
                break
    return array
```



> ### 선택 정렬

- 다음과 같은 순서를 반복하며 정렬하는 알고리즘
  1. 주어진 데이터 중, 최소값을 찾음
  2. 해당 최소값을 데이터 맨 앞에 위치한 값과 교체함
  3. 맨 앞의 위치를 뺀 나머지 데이터를 동일한 방법으로 반복함

```python
def selection_sort(array):
    for i in range(len(array) - 1):
        for j in range(i, len(array)):
            min = array[i]
            if min > array[j]:
                array[i], array[j] = array[j], array[i]
                min = array[j]
    return array
```



>### 퀵 정렬

- 정렬 알고리즘의 꽃
- 기준점(pivot 이라고 부름)을 정해서, 기준점보다 작은 데이터는 왼쪽(left), 큰 데이터는 오른쪽(right) 으로 모으는 함수를 작성함
- 각 왼쪽(left), 오른쪽(right)은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복함
- 함수는 왼쪽(left) + 기준점(pivot) + 오른쪽(right) 을 리턴함

```python
import random

def QuickSort(array):
    if len(array) < 2: # 재귀함수 사용을 위한 base case를 지정
        return array
    
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    bigger = [i for i in array[1:] if i > pivot]

    array = QuickSort(less) + [pivot] + QuickSort(bigger)

    return array
```



> ### 합병 정렬

정렬 알고리즘 방법 중 하나로,

분할 정복 알고리즘을 이용한다.

```bash
# 분할정복 (divide and conquer)
문제를 작은 2개의 문제로 분리하고 각각을 해결한 다음, 결과를 모아서 원래의 문제를 해결하는 전략이다.
```

합병 정렬은 하나의 리스트를 두 개의 균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음,

두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법이다.
합병 정렬은 다음의 단계들로 이루어진다.

1. 분할(Divide): 입력 배열을 같은 크기의 2개의 부분 배열로 분할한다.
2. 정복(Conquer): 부분 배열을 정렬한다. 부분 배열의 크기가 충분히 작지 않으면 순환 호출 을 이용하여 다시 분할 정복 방법을 적용한다.
3. 결합(Combine): 정렬된 부분 배열들을 하나의 배열에 합병한다.

![img](https://blog.kakaocdn.net/dn/bB7p4z/btq8SBS79tD/vnKKDCMpPmEqldf5fHkO50/img.png)



```python
''' divide and conquer 방법으로 부분적으로 나누어 생각한다.
먼저 정렬된 두 리스트를 정렬된 채로 합치는 함수 '''
def merge(list1, list2):
    i = 0
    j = 0

    # 정렬된 항목들을 담을 리스트
    merged_list = []

    # list1과 list2를 돌면서 merged_list에 항목 정렬
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    # list2에 남은 항목이 있으면 정렬 리스트에 추가
    if i == len(list1):
        merged_list += list2[j:]

    # list1에 남은 항목이 있으면 정렬 리스트에 추가
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list

# 합병 정렬
def merge_sort(my_list):
    if len(my_list) < 2:
        return my_list
    
    list1 = my_list[:len(my_list)//2]
    list2 = my_list[len(my_list)//2:]
    
    return merge(merge_sort(list1), merge_sort(list2))
```



>### 힙 정렬

#### 힙이란?

데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)

힙은 완전 이진트리이고, 자식 노드들이 특정한 성질을 가지고 정렬되어 있는 구조이다. 

부모 노드가 자식 노드들보다 크다면 최대 힙(Max Heap)구조라고 하고, 부모 노드가 자식 노드들보다 작다면 최소 힙(Min Heap)구조라고 한다.

#### 힙의 조건

1. 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다. (최대 힙의 경우)
   * 최소 힙의 경우는 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 작음

2. 완전 이진 트리 형태를 가짐

#### 힙 정렬 구현

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



> ### 계수 정렬(Counting Sort)

- `계수 정렬`이라고 부른다.
- 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여 선형 시간에 정렬하는 알고리즘
- data에서 각 항목들의 발생 횟수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열 `count`에 저장한다.

### 카운팅 정렬 과정

1. `counting` 배열에, 주어진 `data` 의 각 요소 출현 횟수를 담는다.
2. `counting` 배열에서 누적 counting을 구한다.
3. `data`의 요소 값을 뒤에서부터 가져와 counting의 값으로 index를 찾고 새로운 빈 배열 `result`에 값을 요소 값을 넣는다. 이 때 누적 counting 값에서 -1을 해준다.

[계수정렬 단계별 애니메이션](https://www.cs.miami.edu/home/burt/learning/Csc517.091/workbook/countingsort.html)

```python
def counting_sort(data, count, result):
    for i in data:
        count[i] += 1   # data 요소의 출현 횟수
    print("count", count)

    for i in range(len(count)-1):
        count[i+1] += count[i]  # 누적 count
    print("누적 count", count)

    for i in range(len(data)-1, -1, -1):
        result[count[data[i]] - 1] = data[i]
        count[data[i]] -= 1
        print("result", result, "count", count)



data = [3, 2, 5, 4, 2, 1, 5, 2, 2, 1]
count = [0 for _ in range(max(data)+1)]   # 최댓값
result = [0 for _ in range(len(data))]  # data 길이만큼
counting_sort(data, count, result)
print(result)
--------------------------------------------------------------
>>> count [0, 2, 4, 1, 1, 2]
>>> 누적 count [0, 2, 6, 7, 8, 10]
>>> result [0, 1, 0, 0, 0, 0, 0, 0, 0, 0] count [0, 1, 6, 7, 8, 10]
>>> result [0, 1, 0, 0, 0, 2, 0, 0, 0, 0] count [0, 1, 5, 7, 8, 10]
>>> result [0, 1, 0, 0, 2, 2, 0, 0, 0, 0] count [0, 1, 4, 7, 8, 10]
>>> result [0, 1, 0, 0, 2, 2, 0, 0, 0, 5] count [0, 1, 4, 7, 8, 9]
>>> result [1, 1, 0, 0, 2, 2, 0, 0, 0, 5] count [0, 0, 4, 7, 8, 9]
>>> result [1, 1, 0, 2, 2, 2, 0, 0, 0, 5] count [0, 0, 3, 7, 8, 9]
>>> result [1, 1, 0, 2, 2, 2, 0, 4, 0, 5] count [0, 0, 3, 7, 7, 9]
>>> result [1, 1, 0, 2, 2, 2, 0, 4, 5, 5] count [0, 0, 3, 7, 7, 8]
>>> result [1, 1, 2, 2, 2, 2, 0, 4, 5, 5] count [0, 0, 2, 7, 7, 8]
>>> result [1, 1, 2, 2, 2, 2, 3, 4, 5, 5] count [0, 0, 2, 6, 7, 8]
>>> [1, 1, 2, 2, 2, 2, 3, 4, 5, 5]
```

---



> ### 기수 정렬(Radix Sort)

* Radix sort(기수정렬)의 기본 아이디어는 각각 자리수끼리 비교해서 정렬을 하는 것이다. 자릿수를 비교할 때는 `counting sort`를 사용 한다. Radix sort에 대해 찾아보면 LSD와 MSD가 있다는 것을 알 수 있다. LSD는 가장 낮은 자릿수부터 비교하면서 정렬을 하는 것이고, MSD는 가장 높은 자릿수부터 비교하면서 정렬을 하는 것이다. 자릿수가 고정되어있기 때문에 `stable`한 알고리즘이다.

* Radix Sort는 `O(kn)`의 시간복잡도를 가지고 있는 정렬 알고리즘이다 (k는 가장 큰 데이터의 자릿수이다). 이 알고리즘이 작동하려면 몇가지의 조건들이 필요하다:

1. 숫자이어야 한다 (ex. ["banana", "apple"] 와 같은 리스트는 정렬 불가)
2. 정수여야 한다 (ex. [12.332, 29.112] 와 같은 리스트는 정렬 불가)

위의 조건들을 만족하지 않으면 Radix sort는 사용할 수 없다. 그리고 `자릿수(k)`의 크기가 클 수록 알고리즘의 속도도 늘어나기 때문에 `k`가 작은 상황일수록 더 빠르게 정렬을 할 수 있다.[
![radix sort](https://devjin-blog.com/static/caa9bdb9287aef86089bfc5beb3f6854/fcda8/radix_sort.png)](https://devjin-blog.com/static/caa9bdb9287aef86089bfc5beb3f6854/f1c64/radix_sort.png)

```python
def countingSort(arr, digit):
    n = len(arr)
  
    # 배열의 크기에 맞는 output 배열을 생성하고 10개의 0을 가진 count란 배열을 생성한다. 
    output = [0] * (n)
    count = [0] * (10)
    
    #digit, 자릿수에 맞는 count에 += 1을 한다. 
    for i in range(0, n):
        index = int(arr[i]/digit) 
        count[ (index)%10 ] += 1
 
    # count 배열을 수정해 digit으로 잡은 포지션을 설정한다.  
    for i in range(1,10):
        count[i] += count[i-1]  
        print(i, count[i])
    # 결과 배열, output을 설정한다. 설정된 count 배열에 맞는 부분에 arr원소를 담는다.   
    i = n - 1
    while i >= 0:
        index = int(arr[i]/digit)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1

    #arr를 결과물에 다시 재할당한다.  
    for i in range(0,len(arr)): 
        arr[i] = output[i]
 
# Method to do Radix Sort
def radixSort(arr):
    # arr 배열중에서 maxValue를 잡아서 어느 digit, 자릿수까지 반복하면 될지를 정한다. 
    maxValue = max(arr)  
    #자릿수마다 countingSorting을 시작한다. 
    digit = 1
    while int(maxValue/digit) > 0: 
        countingSort(arr,digit)
        digit *= 10
 
arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
#arr = [4, 2, 1, 5, 7, 2]
radixSort(arr)
 
for i in range(len(arr)):
    print(arr[i], end=" ")
```



---

## 정렬 알고리즘 비교

![정렬비교.png](../img/정렬비교.png)

---

## 시간복잡도 비교

![img](data:image/png;base64,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)





---



### [Sorting Algorithms Animations](https://www.toptal.com/developers/sorting-algorithms)

\# 다양한 정렬 알고리즘 비교 사이트

---



# List Operations

| Operation           | Code                               | Average Case  |
| :------------------ | :--------------------------------- | :------------ |
| 인덱싱              | `my_list[index]`                   | *O*(1)        |
| 정렬                | `my_list.sort()` `sorted(my_list)` | *O*(*n*lg*n*) |
| 뒤집기              | `my_list.reverse()`                | *O*(*n*)      |
| 탐색                | `element in my_list`               | *O*(*n*)      |
| 끝에 요소 추가      | `my_list.append(element)`          | *O*(1)        |
| 중간에 요소 추가    | `my_list.insert(index, element)`   | *O*(*n*)      |
| 삭제                | `del my_list[index]`               | *O*(*n*)      |
| 최솟값, 최댓값 찾기 | `min(my_list)` `max(my_list)`      | *O*(*n*)      |
| 길이 구하기         | `len(my_list)`                     | *O*(1)        |
| 슬라이싱            | `my_list[a:b]`                     | *O*(*b*−*a*)  |

# Dictionary Operations

| Operation            | Code                   | Average Case |
| -------------------- | ---------------------- | ------------ |
| 값 찾기              | `my_dict[key]`         | *O*(1)       |
| 값 넣어주기/덮어쓰기 | `my_dict[key] = value` | *O*(1)       |
| 값 삭제              | `del my_list[key]`     | *O*(1)       |

