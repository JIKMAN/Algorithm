## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print('|', current.data, end=' | ')
    while current.link != None:
        current = current.link
        print(current.data, end=' | ')
    print()
    
def insert_node(findData, insertData): # 삽입 연산
    global memory, head, current, pre
    current = head
    
    # 찾는 node가 head일 경우
    if findData == head.data: 
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    
     # 찾는 node가 head가 아닌 경우
    while current.link != None:
        node = Node()
        pre = current
        current = current.link
        if current.data == findData:
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    
    # while문 다 돌고나서 현재 current의 위치는 마지막 노드
    node = Node() # 찾는 node가 없는 경우 : 맨 끝에 삽입
    node.data = insertData
    current.link = node
    memory.append(node)

def delete_data(delData):
    global memory, head, current, pre
    current = head

    # 지울 node가 head일 때
    if head.data == delData:    
        head = head.link
        del(current)
        return

    # 지울 node가 head가 아닐 때
    while current.link != None: 
        pre = current
        current = current.link
        if current.data == delData:
            pre.link = current.link
            del(current)
            return


def find_node(findData):
    global memory, head, current, pre
    current = head
    if current.data ==findData:
        return current
    
    while current.link != None:
        current = current.link
        if current.data ==findData:
            return current
    return Node() # 찾는게 없을 경우 빈 노드 반환

## 전역
memory = []
head, current, pre = None, None, None

# 데이터 집합 (실무 DB, 웹크롤링, 센서신호 ...)
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인
# Insert first node into memory
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

# other nodes
for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)

insert_node('다현', '화사')
printNodes(head)
insert_node('범수', '문별')
printNodes(head)

delete_data('화사')
printNodes(head)

fNode = find_node('쯔위')
print(fNode.data)

fNode = find_node('흥민')
print(fNode.data)