## 트리 노드 클래스
class TreeNode():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

## 전역
memory = []
root = None

## 이진트리로 만들 배열
nameArray = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

# 루트 노드 생성
node = TreeNode()
node.data = nameArray[0]
root = node
memory.append(root)

'''이진 탐색 트리 구현'''
for name in nameArray[1:]:
    node = TreeNode()
    node.data = name
    
    current = root
    while True: # 작은 것은 left, 큰 것은 right로 할당
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left # 왼쪽에 이미 있으면 다시 비교
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right # 오른쪽에 이미 있으면 다시 비교

    memory.append(node)

print('이진 탐색 트리 구성 완료')

## 데이터를 탐색할 때 완전 효율적

findlist = ['마마무', '에스파'] # 찾을 이름
for i in findlist:
    findName = i

    current = root
    count = 0

    while True:
        count +=1
        if current.data == findName:
            print(findName, count,'번 만에 찾았다!')
            break
        elif findName < current.data:
            if current.left == None:
                print(findName, '못찾음..')
                break
            current = current.left
        else:
            if current.right == None:
                print('못찾음..')
                break
            current = current.right

