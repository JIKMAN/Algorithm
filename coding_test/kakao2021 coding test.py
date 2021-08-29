#### 1

# 아이디의 길이는 3자 이상 15자 이하여야 합니다.
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
#“네오”는 다음과 같이 7단계의 순차적인 처리 과정을 통해 신규 유저가 입력한 아이디가 카카오 아이디 규칙에 맞는지 검사하고 규칙에 맞지 않은 경우 규칙에 맞는 새로운 아이디를 추천해 주려고 합니다.
# 신규 유저가 입력한 아이디가 new_id라고 한다면,
'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''
import re

new_id = "~!@#$%&*()=+[{]}:?,<>/"

# 1
new_id = new_id.lower()

# 2
p = re.compile(r'[\w\d\-\_\.]')
removed = ""
for i in range(len(new_id)):
    if p.search(new_id[i]):
        removed += new_id[i]
        
# 3
dots = re.findall(r'\.{2,}', removed)
for d in dots:
    removed = removed.replace(d, '.')

# 4
removed = re.sub('^[.]|[.]$', '', removed)

# 5
removed = 'a' if len(removed) == 0 else removed
    

# 6
if len(removed) > 15:
    removed = removed[:15]
    if removed[-1] == '.':
        removed = removed[:-1]

# 7
while len(removed) < 3:
    removed += removed[-1]


#### 2 / 1:08~
'''
[문제]
각 손님들이 주문한 단품 메뉴들이 문자열 형식으로 담긴 배열 orders, “스카피”가 추가하고 싶어 하는 코스요리를 구성하는 단품 메뉴들의 개수가 담긴 배열 course가 매개변수로 주어질 때, “스카피”가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

[제한사항]
orders 배열의 크기는 2 이상 20 이하입니다.
orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
각 문자열은 알파벳 대문자로만 이루어져 있습니다.
각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.
course 배열의 크기는 1 이상 10 이하입니다.
course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
course 배열에는 같은 값이 중복해서 들어있지 않습니다.
정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.
'''

from collections import Counter
from itertools import combinations

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]



def solution(orders, course):
    result = []
    combo_dic = {}

    for c in course:
        for order in orders:
            order = sorted(list(order))
            order = "".join(order)

            tmp = combinations(order, c)
            for i in tmp:         
                new = ''.join(i)
                if new not in combo_dic:
                    combo_dic[new] = 1
                elif new in combo_dic:
                    combo_dic[new] += 1
        if combo_dic == {}:
            continue
        
        max_v = max(combo_dic.values())
        
        for combo in combo_dic:
            if combo_dic[combo] == max_v and combo_dic[combo] > 1:
                result.appe(combo)

        combo_dic = {}
    return sorted(result)



## 다른 풀이
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)


    ## 3

info = ["java backe junior pizza 150","python fronte senior chicken 210","python fronte senior chicken 150","cpp backe senior pizza 260","java backe junior chicken 80","python backe senior chicken 50"]
query = ["java and backe and junior and pizza 100","python and fronte and senior and chicken 200","cpp and - and senior and pizza 250","- and backe and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

# 해당 코드로 효율성을 통과하지 못했다.
def solution3(info, query):
    answer = []
    for q in query:
        cnt = 0
        q = q.split(' ')
        # 0, 2, 4, 6, 7
        for f in info:
            f = f.split(" ")
            if q[0] != f[0] and q[0] != "-":
                continue
            if q[2] != f[1] and q[2] != "-":
                continue
            if q[4] != f[2] and q[4] != "-":
                continue
            if q[6] != f[3] and q[6] != "-":
                continue
            if int(q[7]) <= int(f[4]):
                cnt += 1
            
        answer.appe(cnt)
        
    return answer

# 효율성을 고려한 코드
def solution(info, query):
    answer = []
    info_dict = {}
    
    for x in info:
        li = x.split()
        info_key = li[:-1]
        info_val = int(li[-1]) #score
        for i in range(5):
            for c in combinations(info_key, i):
                tmp_key = ''.join(c)
                if tmp_key in info_dict:
                    info_dict[tmp_key].append(info_val)
                else:
                    info_dict[tmp_key] = [info_val]
                
    for key in info_dict.keys():
        info_dict[key].sort()  #value(score)을 오름차순으로 정렬
        
    # for k, v in info_dict.items():
    #     print(k ,v)
    for qu in query:
        q = qu.split(' ')
        q_score = int(q[-1])
        q_query = q[:-1]
        
        while 'and' in q_query:
            q_query.remove('and')
        while '-' in q_query:
            q_query.remove('-')
        q_query = ''.join(q_query)
        #print(q_query)
        if q_query in info_dict:
            scores = info_dict[q_query]
            if len(scores)>0:
                start, end = 0, len(scores)
                while start < end:
                    mid = (start + end) // 2
                    if scores[mid] >= q_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)
        
    return answer

# print(solution(info, query))


### 4

# 초기 설정
# 1. 지점 C 까지의 거리 + C ~ A 집 까지의 거리 + C ~ B 집 까지의 거리
# 2. 시작 -> A집까지의 거리 + A 집부터 B 집까지의 거리
# 3. 시작 -> B집까지의 거리 + B 집부터 A 집까지의 거리
# 셋 중에 가장 작은 값이 정답일 것이다.

# 해당 코드는 정답은 나오나,, 효율성이 절대 안나온다.

from collections import deque

# [x지점, y지점, 요금]
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
n,s,a,b = 7,3,4,1

from collections import deque

def dfs(array, connection, s, d, n):
    num = [0] * (n+1)
    need = deque()
    visited = []

    need.append(s)

    while need:
        cur = need.popleft()
        visited.append(cur)
        for c in connection[cur]:
            if num[c] == 0:
                num[c] = (num[cur] + array[cur][c])
            if num[c] > (num[cur] + array[cur][c]):
                num[c] = (num[cur] + array[cur][c])
            if c not in visited:
                need.append(c)

    return num[d]


def solution(n, s, a, b, fares):
    array = [[0 for i in range(n+1)] for i in range(n+1)]
    for fare in fares:
        array[fare[0]][fare[1]] = fare[2]
        array[fare[1]][fare[0]] = fare[2]

    connection = {}
    for i in range(1, n+1):
        connection[i] = []
    for fare in fares:
        connection[fare[0]].append(fare[1])
        connection[fare[1]].append(fare[0])

    answer = []
    answer.append(dfs(array, connection, s, a, n) + dfs(array, connection, a, b, n))
    answer.append(dfs(array, connection, s, b, n) + dfs(array, connection, b, a, n))
    for i in range(1, n+1):
        if i == 0 or dfs(array, connection, s, i, n) == 0 :
            continue
        elif i == s:
            answer.append(dfs(array,connection,s,a, n) + dfs(array,connection,s,b, n))
        answer.append(dfs(array, connection, s, i, n) + dfs(array, connection, i, a, n) + dfs(array, connection, i, b, n))
            

    return min(answer)


# print(solution(n,s,a,b,fares))

n,s,a,b =6,4,6,2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# print(solution(n,s,a,b,fares))


#플로이드 워셔 알고리즘 이용(완전탐색)

INF = 200 * 100000 + 1

def floyd(dist, n):
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]




def solution(n, s, a, b, fares):
    dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        dist[i][i] = 0

    for edge in fares:
        dist[edge[0]][edge[1]] = edge[2]
        dist[edge[1]][edge[0]] = edge[2]
    
    floyd(dist, n)
    for i in range(len(dist)):
        print(dist[i])

    answer = INF
    for k in range(n+1):
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])
    return answer



# print(solution(n, s, a, b, fares))

#### 5 - 광고 삽입

'''
다이나믹 프로그래밍 -
전체 구간을 초단위로 나눠 저장

결과 : DP로 하니까 작은 배열에서는 답이 나오는데 메모리가 너무 크면 실패한다....
'''
# 동영상 재생길이 play_time
# 광고의 길이 adv_time
# 시청자 시청 구간정보 logs 
# 광고를 넣을 시작 시간을 retrun (같을 경우 가장 빠른 시각)

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

# play_time 길이로 변환
def time_convert(time: str):
    h = int(time[0:2])
    m = int(time[3:5])
    s = int(time[6:9])
    length = h * 3600 + m * 60 + s
    return length

def reconvert(time: int):
    h = time // 3600
    m = (time % 3600) // 60
    s = (time % 3600) % 60
    if h < 10:
        h = '0' + str(h)
    if m < 10:
        m = '0' + str(m)
    if s < 10:
        s = '0' + str(s)
    return f"{h}:{m}:{s}"


# def solution(play_time, adv_time, logs):
#     dp = [0 for _ in range(time_convert(play_time)+1)]
    
#     for log in logs:
#         log = log.split("-")
#         start = time_convert(log[0])
#         end = time_convert(log[1])
        
#         for i in range(start, end):
#             dp[i] += 1
#     answer = 0
#     idx = 0
#     adv_len = time_convert(adv_time)
#     for i in range(1, len(dp) - adv_len+1):
#         cur = 0
#         for j in range(i, i + adv_len):
#             cur += dp[j]
#         if cur > answer:
#             answer = cur
#             idx = i
#     return reconvert(idx)

## 다른풀이 - DP를 좀더 효율적으로 바꾸면 되는 것..
def solution(play_time, adv_time, logs):
    dp = [0 for _ in range(time_convert(play_time)+1)]
    adv_time = time_convert(adv_time)
    play_time = time_convert(play_time)

    
    for log in logs:
        log = log.split("-")
        start = time_convert(log[0])
        end = time_convert(log[1])
        
        dp[start] += 1
        dp[end] -= 1
    
    for i in range(1, len(dp)):
        dp[i] = dp[i] + dp[i-1]
    for i in range(1, len(dp)):
        dp[i] = dp[i] + dp[i-1]
    
    most_view = 0
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < dp[i] - dp[i - adv_time]:
                most_view = dp[i] - dp[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < dp[i]:
                most_view = dp[i]
                max_time = i - adv_time + 1
    
    return reconvert(max_time)
    
    
        
print(solution(play_time, adv_time, logs))



