## 함수
def openBox():
    global count
    print('박스열기~~')
    count -=1
    if count == 0:
        print("박스에 선물 넣기")
        return
    openBox()
    print('박스 닫기!!')

## 변수
count = 5


## Main
openBox()

def addNum(num):
    if num <= 1:
        return 1
    return num + addNum(num - 1)

print(addNum(10))

def countDown(n):
    if n == 0:
        print('발사!')
    else:
        print(n)
        countDown(n-1)
    
countDown(5)

def printStar(n):
    if n > 0:
        printStar(n-1)
        print('*' * n)
printStar(5)

import random

randomArray = [random.randint(0,255) for _ in range(random.randint(10,20))]

print(randomArray)