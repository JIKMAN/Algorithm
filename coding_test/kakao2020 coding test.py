# -*- coding: utf-8 -*-
# kakao2020 coding test

## 1
'''
데이터 처리 전문가가 되고 싶은 “어피치”는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다. 간단한 예로 “aabbaccc”의 경우 “2a2ba3c”(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, “abcabcdede”와 같은 문자열은 전혀 압축되지 않습니다. “어피치”는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

예를 들어, “ababcdcdababcdcd”의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 “2ab2cd2ab2cd”로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 “2ababcdcd”로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

다른 예로, “abcabcdede”와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 “abcabc2de”가 되지만, 3개 단위로 자른다면 “2abcdede”가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.
'''
s = ['aabbaccc',
     'ababcdcdababcdcd',
     'abcabcdede',
     'abcabcabcabcdededededede',
     'xababcdcdababcdcd',
     'a']

# 5번 케이스만 통과를 못해서 s가 1개일 경우를 따로 지정해 주었다.
import math
from collections import Counter

def solution(s):
    if len(s) == 1:
        return 1

    answer = [0 for i in range(math.ceil(len(s) / 2))]

    for i in range(len(answer)):
        tmp_slice = []
        for j in range(0, len(s), i+1):
            tmp_slice.append(s[j:j+i+1])
        cnt = 1
        result = ""
        for k in range(len(tmp_slice)):
            if k < len(tmp_slice) - 1:
                if tmp_slice[k] == tmp_slice[k+1]:
                    cnt += 1
                else:
                    if cnt == 1:
                        result += tmp_slice[k]
                    else:
                        result += str(cnt) + tmp_slice[k]
                        cnt = 1

            if k == len(tmp_slice)-1:
                if tmp_slice[k] == tmp_slice[k-1]:
                    result += str(cnt) + tmp_slice[k] # s가 1개일 경우 이부분에서 cnt가 붙어서 길이가 2개로 나오게됌..
                else:
                    result += tmp_slice[k]
        answer[i] = len(result)
            
    return min(answer)

# for i in s:
#     print(solution(i))





## 2번

def devide(p):
    u = []
    for i in range(len(p)):
        u.append(p[i])
        if len(u) != 0 and u.count('(') == u.count(')'):
            return p[:i+1], p[i+1:]
    
def perfect(u):
    stack = []
    
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    if perfect(p):
        return p
    u, v = devide(p)
    if perfect(u) == True:
        return u + solution(v)
    else:
        answer ='('
        answer += solution(v)
        answer += ')'
        for w in u[1:len(u) - 1]:
            if w == '(':
                answer += ')'
            else:
                answer += '('
    return answer




## 3

key = [[0, 0, 0], 
       [1, 0, 0], 
       [0, 1, 1]]

lock = [[1, 1, 1], 
        [1, 1, 0], 
        [1, 0, 1]]

## 첫 시도에 실패한 코드, 접근 방법은 비슷했으나 ..

def spin(map): # 정사각형을 회전하는 함수
    new_map = [[0 for i in range(len(map))] for i in range(len(map))]
    for i in range(len(map)):
        for j in range(len(map)):
            new_map[j][len(map)-1-i] = map[i][j]
    return new_map

def push(x, y, array, key):
    for i in range(len(key)):
        for j in range(len(key)):
            array[x+i][y+j] += key[i][j]

def pull(x, y, array, key):
    for i in range(len(key)):
        for j in range(len(key)):
            array[x+i][y+j] -= key[i][j]

def check(array, key, lock):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if array[len(key)+i-1][len(key)+i-1] != 1:
                return False
    return True

def solution(key, lock):
    
    length = len(lock) + len(key) + 1
    array = [[0 for i in range(length)] for i in range(length)]

    for i in range(len(lock)):
        for j in range(len(lock)):
            array[len(key)+i-1][len(key)+j-1] = lock[i][j]

    keys = []
    tmp = key
    for i in range(4):
        keys.append(tmp)
        tmp = spin(tmp)

    for k in keys:
        for x in range(len(key)-1 + len(lock)):
            for y in range(len(key)-1 + len(lock)):

                push(x, y, array, key)

                if check(array, key, lock) == True:
                    return True
                
                pull(x, y, array, key)
    return False

'''
솔루션
1) M*2 + N 크기의 보드를 만들고 중앙에 좌물쇠를 배치한다.
2) key를 4번 돌려가며 차례로 이동시킨다
3) 위에서 아래로 열쇠를 이동했을때 중앙의 키가 모두 1이되면 unlock
def rotate90(arr): # 90도 돌리기
def attach(x, y, M, key, board): # 열쇠 넣어보기
def detach(x, y, M, key, board): # 열쇠 빼기
def check(board, M, N): # 모두 1인지 확인
'''
## 참고하여 바꾼 코드

def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]

def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

def rotate90(arr):
    return list(zip(*arr[::-1])) # 를 통해 한줄로 배열 회전이 가능.. 놀랍다.

def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False;
    return True

def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M*2 + N) for _ in range(M*2 + N)]
    # 자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    rotated_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, M+N):
            for y in range(1, M+N):
                # 열쇠 넣어보기
                attach(x, y, M, rotated_key, board)
                # lock 가능 check
                if(check(board, M, N)):
                    return True
                # 열쇠 빼기
                detach(x, y, M, rotated_key, board)
                
    return False





## 4


# 정답은 전부 통과하나,  효율성 테스트 성공률 20% ,,

import re

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]


def solution(words, queries):
    result = []
    for q in queries:
        q = q.replace('?', '.')
        cnt = 0
        for word in words:
            if re.findall(q, word) and len(q) == len(word):
                cnt += 1
        result.append(cnt)

    return result

# print(solution(words, queries))


# word의 최대 길이도 100,000이고 query의 최대 길이도 100,000이기떄문에 
# 완전탐색으로 돌리면 시간초과가 날 수밖에 없기 때문에 기존에 겹치는 정보는 
# key로 담아주어 시간을 단축시켜주는 trie자료구조를 사용한다
'''
1. 주어진 word를 이용한 trie{}
2. word를 거꾸로 뒤집어 이용한 rev_trie{}
3. 모든 단어의 길이를 센 counted[]
'''
'''
a. '?'로 끝나는 경우(ex:'fr???') : 가장 기본적인 형태입니다. 기본 trie{}를 이용하여 '?'가 나올 때까지 재귀탐색하면 됩니다.

b. '?'로 시작하는 경우(ex:'????o') : 모든 단어를 뒤집어 만든 rev_trie{}와, query 또한 뒤집어서 사용합니다. 반대로 탐색을 한다는 것 외에는 a 조건과 동일합니다. 

c. '?'로만 이루어진 경우 : counted 배열을 이용해서 단순히 길이가 같은 단어들의 갯수를 answer에 삽입합니다. 길이가 같은 모든 단어가 전부 답이 될 수 있기 때문입니다.
'''
# trie를 이용한 다른 사람의 코드

import sys
sys.setrecursionlimit(100001)

def solution(words, queries):
    answer = []
    
    rev_words, counted = [], []   # 조건 b, c를 위한 두 변수
    for w in words:
        rev_words.append(w[::-1])
        counted.append(len(w))

    trie = make_trie({}, words)   # 조건 a 의 trie
    rev_trie = make_trie({}, rev_words)   # 조건 b 의 rev_trie 

    for query in queries:  # 3가지 조건으로 나누어서,
        if query[0] == '?' and query[-1] == '?':
            answer.append(counted.count(len(query)))
        elif query[0] == '?':
            answer.append(search_trie(rev_trie, query[::-1], len(query)))
        elif query[-1] == '?':
            answer.append(search_trie(trie, query, len(query)))

    return answer


def make_trie(trie, words):
    for word in words:
        cur = trie
        l = len(word)
        for w in word:
            if w in cur:
                cur = cur[w]
                cur['!'].append(l)
            else:
                cur[w] = {}
                cur = cur[w]
                cur['!'] = [l]
    return trie


def search_trie(trie, query, length):
    count = 0
    if query[0] == '?':
        return trie['!'].count(length)
    elif query[0] in trie:
        count += search_trie(trie[query[0]], query[1:], length)

    return count


## 5

# 5 <= n <= 100
# (1 ~ 1000) x 4 : [x, y, a, b]
# a = 0 : 기둥, 1 : 보
# b = 0: 삭제, 1 : 설치

# return [x, y, a] -> 위에 기둥 있으면 a = 1, 오른쪽에 보있으면 a = 0
n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

array = [[-1 for i in range(n+1)] for i in range(n)] + [[1 for i in range(n+1)]]


PILLAR, BEAM = 0,1

def solution(n, build_frame):
    answer = []
    for b in build_frame:
        x, y, kind, oper = b
        if oper == 1: # 설치인데
            if kind == PILLAR: # 기둥일 경우
                if pillar_check([x,y], answer):
                    answer.append(b[:3])
            else: # 보일 경우
                if beam_check([x,y], answer):
                    answer.append(b[:3])
        else: # 삭제인데
            temp = answer.copy()
            temp.remove(b[:3])
            check = True
            for t in temp:
                x, y, kind = t
                if kind == PILLAR:
                    if not pillar_check([x,y], temp):
                        check = False
                        break
                else:
                    if not beam_check([x,y], temp):
                        check = False
                        break
            if check:
                answer = temp.copy() 
        
    answer.sort()
    return answer

def pillar_check(pillar_pos, answer):
    x, y = pillar_pos
    if y == 0: # 바닥일 경우는 그냥 설치
        return True
    # 바닥이 아니고 다른 기둥 위에 있거나 보의 한쪽 끝 부분 위에 있는지
    if [x, y-1, PILLAR] in answer or [x-1, y, BEAM] in answer or [x, y, BEAM] in answer:
        return True
    return False

def beam_check(beam_pos, answer):
    x, y = beam_pos
    if [x, y-1, PILLAR] in answer or [x+1, y-1, PILLAR] in answer: # 한쪽 끝 부분이 기둥위에 있거나
        return True
    if [x-1, y, BEAM] in answer and [x+1,y, BEAM] in answer: # 양쪽 끝 부분이 다른 보와 동시에 연결되어 있거나
        return True
    return False



## 6
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

# 가장 많이 걷는 사람 부터
# n 가지 위치에서 출발하여 1을 없앤 다음 없어진 1의 개수를 기록,, 
# 다음 사람을 반복
# 배열에 1이 없으면 끝
# 배열에 1이 있으나 더이상 사람이 없어도 끝


# 필요 라이브러리
from collections import deque


## 빌딩 외벽의 배열
building = [0] * n
for w in weak:
    building[w] = 1
# print(building)

### 현재 건물에서 n가지 출발 위치를 만들어주는 함수###
'''
def start_point(building):
    queue = deque(building)

    start = []
    for i in range(n):  
        tmp = []
        poped = queue.popleft()
        queue.append(poped)
        for q in queue:
            tmp.append(q)
        start.append(tmp)

    return start
    
# 많이 걷는 사람부터 돌거니까 반대로


dist.reverse()

#solution
result = 0
for d in dist:
    start = start_point(building)
    tmp_s = []
    for s in start:
        front = s[:d]
        back = s[-d:]

        if front.count(1) >= back.count(1):
            front = [0] * d
            tmp_s.append(front + s[d:])
        else:
            back = [0] * d
            tmp_s.append(s[:-d] + back)
        
        result += 1
    
    ## 다음 인원으로 넘겨주는 배열 처리가 해결이 안된다.

    # tmp_s 중에 1의 수가 가장 작은것, 1끼리의 거리가 가장 가까운 것
    next_start = []
    num = []
    for idx, t in enumerate(tmp_s):
        num.append([idx, t.count(1)])
    
'''
# 다른 사람의 풀이
from itertools import permutations
def solution(n, weak, dist):
    # 1. 시계 / 반시계 문제 해결하기
    weak_length = len(weak)
    for i in range(weak_length):
        weak.append(weak[i] + n)
    # 4에서 반시계방향 = 9에서 시계방향. 
    # 즉 길이를 두 배 늘려놓으면 굳이 방향 고민할 필요 없다
    
    # 투입할 수 있는 친구의 최댓값. 
    # 점검 불가능한 경우를 상정해서 len(dist) + 1
    answer = len(dist) + 1
    for i in range(weak_length):
        
        # 2. 어디서부터 벽 점검을 시작할 것인지 결정
        start_point = [weak[j] for j in range(i, i + weak_length)]
        
        # 3. 벽 점검에 투입할 친구의 순서 정하기
        candidates = permutations(dist, len(dist))
        
        # 4. 탐색
        for order in candidates:
            # 순서대로 출발. 
            friend_idx, friend_count = 0, 1
            # 친구가 확인할 수 있는 최대 거리
            possible_check_length = start_point[0] + order[friend_idx]
            
            for idx in range(weak_length):
                # 확인할 수 있는 최대 거리를 넘어설 경우
                if start_point[idx] > possible_check_length:
                    # 다음 친구 투입
                    friend_count += 1
                    # 더 이상 투입할 친구가 없는 경우 break
                    if friend_count > len(order):
                        break
                    # 다음 친구 투입, 친구가 확인할 수 있는 최대 거리 업데이트
                    friend_idx += 1
                    possible_check_length = order[friend_idx] + start_point[idx]
            # 투입할 친구 최솟값 업데이트                     
            answer = min(answer, friend_count)
    
    if answer > len(dist):
        return -1
    
    return answer 