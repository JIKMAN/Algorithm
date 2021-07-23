# 알고리즘

- 탐색 알고리즘
  - [선형 탐색](#선형탐색)
- 재귀 함수
- Brute Force
- Divide and Conquer
- Dynamic Programming
- Greedy Algorithm



## 탐색 알고리즘

> ### 선형탐색

리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘

```python
# 해당 element가 list에 존재하면 해당 element의 index를 리턴
def linear_search(element, list):
    for i in range(len(list)):
        if element == list[i]:
            return i
    return None
```



