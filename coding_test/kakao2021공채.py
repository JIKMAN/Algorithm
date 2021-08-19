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



## 2 엄청 지저분하지만.. 일단 답은 맞음.. 50분 소요

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
    
cachSize = 3
cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
print(solution3(cities, cachSize))

cachSize = 3
cities2 = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
print(solution3(cities2, cachSize))

cachSize = 2
cities3 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
print(solution3(cities3, cachSize))

cachSize = 5
cities4 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']
print(solution3(cities4, cachSize))

cachSize = 2
cities5 = ['Jeju', 'Pangyo', 'NewYork', 'newyork']
print(solution3(cities5, cachSize))

cachSize = 0
cities6 = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']  
print(solution3(cities6, cachSize))

