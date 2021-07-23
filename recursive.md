# 재귀 함수

- 함수 안에서 동일한 함수를 호출하는 형태의 함수



재귀함수 예시

```python
# 팩토리얼

def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num
---------------------------------------
0
1
2
6
24
120
720
5040
40320
362880
```

---



```python
# 카운트다운

def countDown(n):
    if n == 0:
        print('발사!')
    else:
        print(n)
        countDown(n-1)
-------------------------------
5
4
3
2
1
발사!    
```

---



```python
# 별 그리기

def printStar(n):
    if n > 0:
        printStar(n-1)
        print('*' * n)
printStar(5)
---------------------------------
*
**
***
****
*****
```

---



```python
# 재귀함수로 이진 탐색 구현

def binary_search(element, array, start=0, end=None):
    if end == None:
        end = len(array) - 1

    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if array[mid] == element:
        return mid
        
    if element < array[mid]:
        return binary_search(element, array, start, mid - 1)
        
    else:
        return binary_search(element, array, mid + 1, end)
```

---



![img](https://upload.wikimedia.org/wikipedia/commons/6/60/Tower_of_Hanoi_4.gif)

```python
# 하노이의 탑

def move_disk(disk_num, start, end):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start, end))

def hanoi(num_disks, start, end): # 1번위치 2번위치 3번위치의 인덱스 합은 항상 6
    if num_disks == 0:
        return
    else:
        other = 6 - start - end
    
        hanoi(num_disks - 1, start, other)
        move_disk(num_disks, start, end)
        hanoi(num_disks - 1, other, end)
hanoi(3, 1, 3) # 3개의 원판을 1번에서 3번으로 이동
--------------------------------------------------------------
>>> 1번 원판을 1번 기둥에서 3번 기둥으로 이동
>>> 2번 원판을 1번 기둥에서 2번 기둥으로 이동
>>> 1번 원판을 3번 기둥에서 2번 기둥으로 이동
>>> 3번 원판을 1번 기둥에서 3번 기둥으로 이동
>>> 1번 원판을 2번 기둥에서 1번 기둥으로 이동
>>> 2번 원판을 2번 기둥에서 3번 기둥으로 이동
>>> 1번 원판을 1번 기둥에서 3번 기둥으로 이동
```

