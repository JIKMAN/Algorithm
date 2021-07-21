## 함수
def add_data(name):
    katok.append(None)
    kLen = len(katok)
    katok[kLen - 1] = name

def insert_data(position, name):
    katok.append(None)

    for i in range(len(katok)-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[position] = name

def delete_data(position):
    kLen = len(katok)
    katok[position] = None

    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
    
    del(katok[kLen - 1])
    

## 전역
select = -1 # 1 : 추가, 2: 삽입, 3: 삭제, 4 : 종료
katok = []


## 메인
while select != 4:
    
    select = int(input('선택(1 : 추가, 2: 삽입, 3: 삭제, 4 : 종료)'))
    
    if select == 1:
        name = input('추가할 사람 -> ')
        add_data(name)
        print(katok)
    elif select == 2:
        insert_data(int(input('원하는 자리 : ')), input('넣을 사람 : '))
        print(katok)
    elif select == 3:
        delete_data(int(input('지울 자리 : ')))
        print(katok)
    elif select == 4:
        pass # 종료
    else:
        print('잘못 입력!')