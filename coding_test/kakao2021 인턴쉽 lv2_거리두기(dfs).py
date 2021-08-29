'''
문제 2
문제 풀이 : Lv2. 거리 두기 확인하기

개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.
코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야 하는데 개발 직군 면접인 만큼 아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.

1. 대기실은 5개이며, 각 대기실은 5×5 크기입니다.
2. 거리 두기를 위하여 응시자들 끼리는 맨해튼 거리가 2 이하로 앉지 말아 주세요.
3. 단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

✔ 맨해튼 거리: 두 테이블 T1, T2가 행렬 (r1, c1), (r2, c2)에 각각 위치하고 있다면, T1, T2 사이의 맨해튼 거리는 |r1 – r2| + |c1 – c2|입니다.

예를 들어,


5개의 대기실을 본 죠르디는 각 대기실에서 응시자들이 거리 두기를 잘 기키고 있는지 알고 싶어졌습니다. 자리에 앉아있는 응시자들의 정보와 대기실 구조를 대기실별로 담은 2차원 문자열 배열 places가 매개변수로 주어집니다. 각 대기실별로 거리 두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

제한사항
places의 행 길이(대기실 개수) = 5
places의 각 행은 하나의 대기실 구조를 나타냅니다.
places의 열 길이(대기실 세로 길이) = 5
places의 원소는 P,O,X로 이루어진 문자열입니다.
places 원소의 길이(대기실 가로 길이) = 5
P는 응시자가 앉아있는 자리를 의미합니다.
O는 빈 테이블을 의미합니다.
X는 파티션을 의미합니다.
입력으로 주어지는 5개 대기실의 크기는 모두 5×5 입니다.
return 값 형식
1차원 정수 배열에 5개의 원소를 담아서 return 합니다.
places에 담겨 있는 5개 대기실의 순서대로, 거리 두기 준수 여부를 차례대로 배열에 담습니다.
각 대기실 별로 모든 응시자가 거리 두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 담습니다.
'''
from collections import deque


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

D = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs(place, x, y):
    visited = [[False for _ in range(5)] for _ in range(5)]
    q = []
    visited[x][y] = True
    q.append((x, y, 0))

    while q:
        cur = q.pop()

        if cur[2] > 2:
            continue
        if cur[2] != 0 and place[cur[0]][cur[1]] == 'P':
            return False
        
        for i in range(4):
            nx = x + D[i][0]
            ny = y + D[i][1]
            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue
            if visited[nx][ny]:
                continue
            if place[nx][ny] == 'X':
                continue
            visited[nx][ny] = True
            q.append((nx, ny, cur[2] + 1))
    return True



def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if bfs(place, i, j) == False:
                    return False
    return True

def solution(places):
    answer = []

    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer

print(solution(places))