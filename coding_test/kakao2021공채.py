## 1 맞음.. 30분 소요

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]



def make_2nd(a):
    b = ""
    while a >= 1:    
        b = '01'[a%2] + b
        a //= 2

    while len(b) < n:
        b = str(0) + b

    return b

def solution(n, arr1, arr2):
    arr1 = [list(make_2nd(arr1[i])) for i in range(len(arr1))]
    arr2 = [list(make_2nd(arr2[i])) for i in range(len(arr2))]

    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '1':
                arr1[i][j] = '#'
            elif arr1[i][j] == '1':
                arr1[i][j] = '#'
    for i in range(len(arr1)):
        arr1[i] = "".join(arr1[i])
        arr1[i] = arr1[i].replace('0', ' ')
        
    return arr1

# print(solution(n, arr1, arr2))

n = 6
test_arr1 = [46, 33, 33 ,22, 31, 50]
test_arr2 = [27 ,56, 19, 14, 14, 10]

# print(solution(n, test_arr1, test_arr2))

### 2진수 변환 -> bin(숫자)



## 2 엄청 지저분하지만.. 일단 답은 맞음.. 60분 소요

dart = '1S2D*3T'
dart2 = '1D2S#10S'
dart3 = '1D2S0T'
dart4 = '1S*2T*3S'
dart5 = '1D#2S*3S'
dart6 = '1T2D3D#'
dart7 = '1D2S3T*'

def solution2(dart):
    answer = 0
    dart = list(dart)
    
    tmp_idx = []
    for i in range(len(dart)-1):
        if dart[i].isdigit() == True and dart[i+1].isdigit() == True:
            dart[i] = dart[i] + dart[i+1]
            tmp_idx.append(i+1)
        if dart[i].isdigit() == False and dart[i+1].isdigit() == False:
            dart[i] = dart[i] + dart[i+1]
            tmp_idx.append(i+1)
       
    tmp_idx.sort(reverse=True)
    
    cnt = 0
    for i in range(len(tmp_idx)):
        dart.remove(dart[tmp_idx.pop() - cnt])
        cnt += 1
     

    for i in range(0, len(dart), 2):
        if len(dart[i+1]) == 1:
            if dart[i+1] == 'S':
                dart[i] = dart[i]
            elif dart[i+1] == 'D':
                dart[i] = int(dart[i]) ** 2
            else:
                dart[i] = int(dart[i]) ** 3
    
        if len(dart[i+1]) == 2:
            if dart[i+1][1] == "*":
                if i == 0:
                    if dart[i+1][0] == 'S':
                        dart[i] = int(dart[i]) * 2
                    elif dart[i+1][0] == 'D':
                        dart[i] = (int(dart[i]) ** 2) * 2
                    else:
                        dart[i] = (int(dart[i]) ** 3) * 2
                else:
                    if dart[i+1][0] == 'S':
                        dart[i] = int(dart[i]) * 2
                    elif dart[i+1][0] == 'D':
                        dart[i] = (int(dart[i]) ** 2) * 2
                    else:
                        dart[i] = (int(dart[i]) ** 3) * 2
                    dart[i-2] = int(dart[i-2]) * 2

      
            elif dart[i+1][1] == "#":
                if dart[i+1][0] == 'S':
                    dart[i] = int(dart[i]) * (-1)
                elif dart[i+1][0] == 'D':
                    dart[i] = (int(dart[i]) ** 2) * (-1)
                else:
                    dart[i] = (int(dart[i]) ** 3) * (-1)
    
    for i in range(0, len(dart), 2):
        answer += int(dart[i])  

    return answer



# print(solution2(dart))
# print(solution2(dart2))
# print(solution2(dart3))
# print(solution2(dart4))
# print(solution2(dart5))
# print(solution2(dart6))
# print(solution2(dart7))

## 3 - 얘도 답은 나왔음.. 30분

from collections import deque
from re import template

def solution3(cities, cacheSize):
    result = 0
    cachelist = deque()

    for city in cities:
        city = city.upper()
        if city not in cachelist:
            result += 5

            if len(cachelist) >= cacheSize and len(cachelist) != 0:
                cachelist.popleft()
                cachelist.append(city)

            else:
                cachelist.append(city)
        else:
            result += 1
    return result
    
# cachSize = 3
# cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
# print(solution3(cities, cachSize))

# cachSize = 3
# cities2 = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
# print(solution3(cities2, cachSize))

# cachSize = 2
# cities3 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
# print(solution3(cities3, cachSize))

# cachSize = 5
# cities4 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
# print(solution3(cities4, cachSize))

# cachSize = 2
# cities5 = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
# print(solution3(cities5, cachSize))

# cachSize = 0
# cities6 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']  
# print(solution3(cities6, cachSize))



## 4

# 09:00시 부터 n회 t분 마다 m명 탈수있음
# 셔틀을 타고 갈수있는 도착 시간 중 제일 늦은 시간

# 하루 동안 크루가 대기열에 도착하는 시각

## 으아... 답이 안나오네... pass

'''
1. 탑승자 timetable 숫자로 변환
2. 버스 리스트 해시 테이블 {bus1 : [], bus2 : []}
2. 숫자 변환 clock 함수
4. 버스 목록에서 popleft, 버스 리스트 승객 꽉찼으면 다음 버스 목록 popleft
   자리가 남아 있으면 제일 마지막 사람과 같은 시간
   마지막 버스까지 자리가 꽉차있으면 제일 마지막 사람 시간 -1분
'''


from collections import deque

def clock(pre, t): # 시간 구하는 함수
    hour = pre // 100
    min = pre % 100

    if min + t >= 60:
        hour += (min + t) // 60
        min = (min + t) % 60
    else:
        min = min + t
    cur_time = hour * 100 + min

    return cur_time


def solution4(n, t, m, timetable):

    for i in range(len(timetable)):
        timetable[i] = int(timetable[i][:2]+timetable[i][3:])
    timetable.sort()
    timetable = deque(timetable)

    bus_dic = {}
    bus_list = deque()
    depart_time = 900
    for i in range(n): 
        bus_dic[depart_time] = []
        bus_list.append(depart_time)
        depart_time = clock(depart_time, m)


    answer = 0
    while bus_list:
        if len(timetable) == 0:
            break
        tmp = bus_list.popleft()
        while timetable:
            if len(bus_dic[tmp]) < m and tmp >= timetable[0]:
                person = timetable.popleft()
                bus_dic[tmp].append(person)
            else:
                break
        
        if len(bus_list) == 0:
            last_bus = max(bus_dic.keys())
            last_person = max(bus_dic[last_bus])
            # 모든 버스 자리 꽉찬경우
            if bus_dic[last_bus] == m:
                answer = clock(last_person, -1)
            else:
                answer = last_bus     
        # 버스 자리 남은 경우
        else:
            answer = max(bus_list)

    return answer

timetable = ['08:00', '08:01', '08:02', '08:03', '09:02']
# print(solution4(1,1,5, timetable))




## 5

from collections import Counter

def make_dic(str1):
    str_list = []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() == False or str1[i+1].isalpha() == False:
            continue
        str_list.append(str1[i:(i+2)].upper())

    str_dic = Counter(str_list)

    return str_dic

def solution5(str1, str2):
    whole = 0
    part = 0

    first_dic = make_dic(str1)
    second_dic = make_dic(str2)

    for str in first_dic:
        if str in second_dic:
            whole += max(first_dic[str], second_dic[str])
            part += min(first_dic[str], second_dic[str])
        else:
            whole += first_dic[str]
    
    for str in second_dic:
        if str not in first_dic:
            whole += second_dic[str]

    if whole == 0:
        similarity = 65536
    else:
        similarity = int(part / whole * 65536)


    return similarity

# str1 = "FRANCE"
# str2 = "french"
# print(solution5(str1, str2))

# str1 = "handshake"
# str2 = "shake hands"
# print(solution5(str1, str2))

# str1 = "aa1+aa2"
# str2 = "AAAA12"
# print(solution5(str1, str2))

# str1 = "E=M*C^2"
# str2 = "e=m*c^2"
# print(solution5(str1, str2))


## 6 
# 1시간 20분 걸림............. 성공하긴 했는데 많이 지저분 함...
# 다른 풀이 보고 업데이트 해야겠음

m = 6
n = 6
board = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']

def pang(board):
    idx = []
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if board[i][j] == board[i+1][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j+1]:
                idx.append([i,j])
    if len(idx) == 0:
        return False

    for i in range(len(idx)):
        a = idx[i][0]
        b = idx[i][1]

        board[a][b], board[a][b+1], board[a+1][b], board[a+1][b+1] = 0,0,0,0
    
    temp_board = []
    for i in range(len(board[0])):
        temp_list = []
        for j in range(len(board)):
            temp_list.append(board[j][i])
        cnt = 0
        while 0 in temp_list:
            temp_list.remove(0)
            cnt += 1
        while cnt != 0:
            temp_list.insert(0, 0)
            cnt -= 1
        temp_board.append(temp_list)

    for i in range(len(temp_board)):
        for j in range(len(temp_board[0])):
            board[j][i] = temp_board[i][j]

    return board

def last_pang(board):
    
    board = [list(b) for b in board]


    while not False:
        answer = pang(board)
        return pang(answer)
    

def solution6(board):
    last = last_pang(board)
    cnt = 0
    
    for i in range(len(last)):
        for j in range(len(last[0])):
            if last[i][j] == 0:
                cnt += 1

    return cnt

# print(solution6(board))

board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
# print(solution6(board))


## 7 추석 트래픽

# 임의 시간부터 1초간 처리하는 요청의 최대 개수
# line 배열 = (1~2000)개의 로그 문자열 S : 응답 완료시간, T: 처리시간
# S는 고정길이의 timestamp 형식으로 되어있다.
# T는 최대 소수점 셋째자리로 구성된 초 단위 0.000s
# 처리시간은 0.001 ~ 3.000

## 포기 ......

data = ['2016-09-15 01:00:04.001 2.0s', '2016-09-15 01:00:07.000 2s']

def solution7(data):
    start = []
    end = []
    for d in data:
        d = [d[11:13] +d[14:16] + d[17:19] + d[20:23], d[24] + d[26:-1]]
        while len(d[1]) != 4:
            d[1] += '0'
        tmp = int(d[1])
        d[1] = int(d[0])
        d[0] = int(d[0]) - tmp + 1
        start.append(d[0])
        end.append(d[1])
    
    answer = 0
    for i in range(len(data)):
        cnt = 0
        cur_end = end[i]
        for j in range(i, len(data)):
            if cur_end > start[j] - 1000:
                cnt += 1
        answer = max(answer, cnt)
    return answer    
    # result = 0
    # big = 0
    # small = 1000000000
    # for i in range(len(new_data)):
    #     if new_data[i][1] > big:
    #         big = new_data[i][1]
    #     if new_data[i][0] < small:
    #         small = new_data[i][0]
    # print(new_data)
    # time = [0 for i in range(big - small + 1)]

    # for i in range(len(time) - 1000):
    #     for j in range(len(new_data)):
    #         front = new_data[j][0] - small
    #         back = new_data[j][1] - small
    #         if back <= i or front > i + 1000:
    #             continue
    #         else:
    #             time[i] += 1

    # return max(time)

    # print(len(time))
    # print(new_data)

print(solution7(data))
data = [ '2016-09-15 01:00:04.002 2.0s', '2016-09-15 01:00:07.000 2s']
print(solution7(data))
data = [ '2016-09-15 20:59:57.421 0.351s', '2016-09-15 20:59:58.233 1.181s', '2016-09-15 20:59:58.299 0.8s', '2016-09-15 20:59:58.688 1.041s', '2016-09-15 20:59:59.591 1.412s', '2016-09-15 21:00:00.464 1.466s', '2016-09-15 21:00:00.741 1.581s', '2016-09-15 21:00:00.748 2.31s', '2016-09-15 21:00:00.966 0.381s', '2016-09-15 21:00:02.066 2.62s' ]
print(solution7(data))

