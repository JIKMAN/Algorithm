# -*- coding: utf-8 -*-
"""202130503

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SXwydKjvVNrUHebzCXAgiK1QDyCC9QXm
"""

def exam1(arr, name, score):
    arr.append((name, score))
    return sorted(arr, key=lambda x: x[1], reverse=True)

def exam2(arr):
    cnt = 0
    for idx in range(len(arr)):
        min = idx
        for j in range(idx, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if min != idx:
            arr[idx], arr[min] = arr[min], arr[idx]
            cnt += 1
    return cnt

def exam3(weight):
    dp = [0,0,0,6,8,12,13]
    if weight < 7:
        return dp[weight]
    for i in range(7, weight + 1):
        m1 = dp[i - 1]
        m3 = dp[i - 3] + dp[3]
        m4 = dp[i - 4] + dp[4]
        m5 = dp[i - 5] + dp[5]
        m6 = dp[i - 6] + dp[6]
        max_val = max(m1, m3, m4, m5, m6)
        dp.append(max_val)
    return dp[weight]

from collections import deque

def exam4(n, k):
    q = deque([i for i in range(1, n + 1)])
    while q:
        if len(q) == 1:
            return q[0]
        for i in range(k):
            tmp = q.popleft()
            if i != k-1:
                q.append(tmp)

def exam5(arr, n):
    arr.sort()
    start = 0
    end = len(arr) - 1
    cnt = 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == n:
            return cnt
        elif arr[mid] < n:
            start = mid + 1
        else:
            end = mid -1
        cnt += 1