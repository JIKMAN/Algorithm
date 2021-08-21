'''2019 kakao blind recruitment'''

## 1. 오픈채팅방 - 
'''~22분 통과'''

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]


def solution(record):
    result = []
    name_dic = {}
    answer = []

    for i in range(len(record)):
        record[i] = record[i].split(" ")
        r = record[i]

        if r[0] == 'Change' or r[0] == 'Enter':
            name_dic[r[1]] = r[2]
        
        if r[0] == 'Enter' or r[0] == 'Leave':
            result.append(r)

    for i in range(len(result)):
        if result[i][1] in name_dic:
            if result[i][0] == 'Enter':
                answer.append(f'{name_dic[result[i][1]]}님이 들어왔습니다.')
            else:
                answer.append(f'{name_dic[result[i][1]]}님이 나갔습니다.')
        
        
    return answer

    
## 2. 실패율

# 전체 스테이지 개수 N (1 ~ 500)
# 실패율 = 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 현재 멈춰있는 스테이지 배열 stages(1 ~ 200,000)
# 실패율 높은 스테이지부터 내림차순으로 return


''' 통과는 했으나 효율성이 떨어져 보임.. ~52분'''

N = 5
stages = 	[2, 1, 2, 6, 2, 4, 3, 3]

def solution2(N, stages):
    answer = []
    stop = [0 for i in range(N+1)]

    for i in range(1, N+2):
        stop[i-1] = stages.count(i)

    
    for i in range(len(stop)):
        if stop[i] == 0:
            stop[i] = [i+1, 0]
        else:
            stop[i] = [i+1, stop[i] / sum(stop[i:])]
    
    stop.pop()
    stop.sort(key= lambda x: x[1], reverse=True)

    for i in range(len(stop)):
        answer.append(stop[i][0])
        
    return answer


## 3 pass

from itertools import combinations
from collections import Counter

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]




# print(columns)



def remove_unique(columns):
    removed_columns = []
    for i in range(len(columns)):
            if len(columns[i]) != len(set(columns[i])):
                removed_columns.append(columns[i])
    return removed_columns



def solution(relation):
    answer = 0
    columns = [[] for i in range(len(relation[0]))]

    for i in range(len(relation)):
        for j in range(len(relation[0])):
            columns[j].append(relation[i][j])
    print(columns)

    for i in range(len(columns)):
        if len(columns[i]) == len(set(columns[i])):
            answer += 1

    print(answer)

    new_columns = list(combinations(remove_unique(columns), 2))
    print(new_columns)
    print()

    for c in new_columns:
        combi = []
        for i in range(len(c[0])):
            tmp = []
            for j in range(len(c)):
                tmp.append(c[j][i])
            combi.append(tmp)
        print(combi)

# print(solution(relation))

''' 포기 ...... ~2시간'''


## 4

# N 개의 음식
# 1번부터 섭취
# 마지막음식 섭취 후 다시 1번
# 음식 1초 섭취 후 남기고 다음 음식으로
# 먹방 시작 K초 후 방송 중단

# 각 섭취에 걸리는 시간 배열 food_times = []
# K초가 주어졌을 때 몇번 음식부터 섭취하면 되는지 return


# 왜 안되는지 모르겠네ㅠㅠㅠㅠㅠㅠㅠ

'''
from collections import deque

food_time = [3, 1, 2]
k = 5

def solution4(food_time, k):
    food_idx = deque()
    for idx, food in enumerate(food_time):
        food_idx.append([idx + 1, food])
    result = k
    zero_cnt = []
    while k > 0 :
        if len(zero_cnt) == len(food_idx):
            return -1
        if food_idx[0][1] != 0:
            food_idx[0][1] -= 1
            poped = food_idx.popleft()
            food_idx.append(poped)
            k -= 1
            continue
        else:
            zero_cnt.append(food_idx[0][0])
            poped = food_idx.popleft()
            food_idx.append(poped)

    while food_idx[0][1] == 0:
        poped = food_idx.popleft()
        food_idx.append(poped)

    return food_idx[0][0]



print(solution4(food_time, k))
'''
 




## 5
'''
nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
   
class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


tmp_layer = [[] for j in range(max(i[1] for i in nodeinfo) + 1)]
layer = []
for i in range(len(nodeinfo)):
    tmp_layer[nodeinfo[i][1]].append(nodeinfo[i][0])

for i in range(len(tmp_layer)):
    if len(tmp_layer[i]) != 0:
        layer.append(sorted(tmp_layer[i]))
        


print(layer)

# 루트 노드 생성
memory = []

node = TreeNode()
node.data = layer[-1]
root = node
print(node.data)

for i in range(len(layer)-1, 0, -1):
    tmp = layer[i] + layer[i-1]
    
    for j in range(len(tmp)):
        node.data
'''


## 6

# 기본점수, 
# 노드 링크점수 = (기본점수 / 다른 노드로 연결 보내는 외부링크 수),
# 해당 웹페이지의 링크점수 = 연결된 노드들의 링크점수의 합
# 웹페이지의 매칭점수 = 기본점수 + 링크점수
# 매칭점수가 가장 높은 웹페이지의 index, 여러개라면 그중 가장 작은 것

# 1 <= len(pages) <= 20,
# 웹페이지 문자열 길이 < 1500
# pages = 웹페이지들의 배열
# 모든 외부 링크는 <a href=”https://careers.kakao.com/index”>
# word <= 12, 대문자 구별 x

## 내 코드는 구현이 안되는 테스트가 몇개 있다

import re



pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

word = 'blind'

def solution(word, pages):
    page_dic = {}

    for i in range(len(pages)):
        link_start = re.search('content="https://', pages[i])
        link_end = re.search('</head>', pages[i])
        link = pages[i][link_start.end():(link_end.start()-4)]
        page_dic[link] = [i,0,0,0,0]

    for i in range(len(pages)):
        link_start = re.search('content="https://', pages[i])
        link_end = re.search('</head>', pages[i])
        link = pages[i][link_start.end():(link_end.start()-4)]

        m = re.findall(rf'[\d|\s]+({word})[\d|\s]+', pages[i], re.I)
        page_dic[link][1] = len(m)

        out_link = re.findall('<a href', pages[i])
        for o in out_link:
            page_dic[link][2] += 1

        page_dic[link][3] = page_dic[link][1] / page_dic[link][2]
        page_dic[link][4] += page_dic[link][1]

        for i in range(len(pages)):
            outer_link = re.findall(r'<a href="(https://[\S]*)"', pages[i])
            
            for o in outer_link:
                if o in page_dic:
                    page_dic[o][4] += page_dic[link][3]
        
    page_list = []
    for page in page_dic:
        page_dic[page] = [page_dic[page][0], page_dic[page][4]]
        page_list.append(page_dic[page])

    big_idx = max(page_list, key=lambda x: x[1])

    return big_idx[0]


# print(solution(word, pages))


# 다른것을 참고하여 다시만든 코드 .

import re

def solution(word, pages):
    webpage = []
    webpageName = []
    webpageGraph = dict() # 나를 가리키는 외부 링크
    
    for page in pages:
        url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        basicScore = 0
        for f in re.findall(r'[a-zA-Z]+', page.lower()):
            if f == word.lower():
                basicScore += 1
        exiosLink = re.findall('<a href="(https://[\S]*)"', page)
        
        for link in exiosLink:
            if link not in webpageGraph.keys():
                webpageGraph[link] = [url]
            else:
                webpageGraph[link].append(url)
        
        webpageName.append(url)
        webpage.append([url, basicScore, len(exiosLink)]) # 내가 가진 외부 링크 (개수)
        
    # 링크점수 = 해당 웹페이지로 링크가 걸린 다른 웹페이지의 기본점수 ÷ 외부 링크 수의 총합
    # 매칭점수 = 기본점수 + 링크점수
    maxValue = 0
    result = 0
    for i in range(len(webpage)):
        url = webpage[i][0]
        score = webpage[i][1]
        
        if url in webpageGraph.keys():
            # 나를 가리키는 다른 링크의 기본점수 ÷ 외부 링크 수의 총합을 구하기 위해
            for link in webpageGraph[url]: 
                a, b, c = webpage[webpageName.index(link)]
                score += (b / c)
        
        if maxValue < score:
            maxValue = score
            result = i
    
    return result



## 7 - 블록게임

# 1. 현재 board에 위에서부터 비어있는 모든 칸에 검은 블록(-1으로 임의 지정)을 채운다.
# 2. 숫자 4개 + 검은 블록 2개(5가지 경우의 수)로 직사각형이 만들어진 경우 삭제!, count + 1

board = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,4,0,0,0],
         [0,0,0,0,0,4,4,0,0,0],
         [0,0,0,0,3,0,4,0,0,0],
         [0,0,0,2,3,0,0,0,5,5],
         [1,2,2,2,3,3,0,0,0,5],
         [1,1,1,0,0,0,0,0,0,5]]
# 1
for i in range(len(board[0])):
    for j in range(len(board)):
        if board[j][i] == 0:
            board[j][i] = -1
        else:
            break

# 2 - 지울 블록을 찾고 있다면 지우고 없으면 False를 return
count = 0
for i in range(len(board)-1):
    for j in range(len(board[0])):
        if board[i][j] != -1 and board[i][j] != 0:
            # j가 맨 앞일 경우 경우의수 2개, 끝일 경우 2개
            if j == 0:
                if board[i][j] == board[i][j+1] and board[i+1][j] == -1 and board[i+1][j+1] == -1:
                    board[i][j], board[i][j+1], board[i][j+2], board[i+1][j+2] = -1, -1, -1, -1
                    count += 1
                elif board[i][j] == board[i][j+1] == board[i+1][j+1] == board[i+1][j+2] and board[i+1][j] == -1 and board[i+2][j] == -1:
                    board[i][j], board[i][j+1], board[i+1][j+1], board[i+1][j+2] == -1, -1, -1, -1
                    count += 1
        

            elif j == len(board[0]):
                if board[i][j] == board[i][j+1] and board[i-1][j] == -1 and board[i-1][j+1] == -1:
                    board[i][j], board[i][j+1], board[i][j+2], board[i-1][j+2] = -1, -1, -1, -1
                    count += 1
                elif board[i][j] == board[i][j+1] == board[i-1][j+1] == board[i-1][j+2] and board[i-1][j] == -1 and board[i-2][j] == -1:
                    board[i][j], board[i][j+1], board[i-1][j+1], board[i-1][j+2] = -1, -1, -1, -1
                    count += 1
            if board[i][j] == board[i][j+1] and board[i+1][j] == -1 and board[i+1][j+1] == -1:
                board[i][j], board[i][j+1], board[i][j+2], board[i+1][j+2] = -1, -1, -1, -1
                count += 1
            elif board[i][j] == board[i][j+1] == board[i+1][j+1] == board[i+1][j+2] and board[i+1][j] == -1 and board[i+2][j] == -1:
                board[i][j], board[i][j+1], board[i+1][j+1], board[i+1][j+2] == -1, -1, -1, -1
                count += 1
            elif board[i][j] == board[i][j+1] and board[i-1][j] == -1 and board[i-1][j+1] == -1:
                board[i][j], board[i][j+1], board[i][j+2], board[i-1][j+2] = -1, -1, -1, -1
                count += 1
            elif board[i][j] == board[i][j+1] == board[i-1][j+1] == board[i-1][j+2] and board[i-1][j] == -1 and board[i-2][j] == -1:
                board[i][j], board[i][j+1], board[i-1][j+1], board[i-1][j+2] = -1, -1, -1, -1
                count += 1
            elif board[i][j] == board[i][j+1] == board[i-1][j+1] == board[i-1][j+1] and board[i-1][j] == -1 and board[i+1][j] == -1:
                board[i][j], board[i][j+1], board[i-1][j+1], board[i-1][j+1] = -1, -1, -1, -1
                count += 1

for b in board:
    print(b)