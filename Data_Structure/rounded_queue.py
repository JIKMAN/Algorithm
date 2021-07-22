## 함수
def isQueueFull(): # 큐가 가득 찼는지 확인하는 함수
    global SIZE, queue, front, rear
    if (rear + 1) % SIZE == front:
        return True
    else:
        return False

def isQueueEmpty(): # 큐가 비었는지 확인하는 함수
    global SIZE, queue, front, rear
    if rear == front:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull() == True:
        print('큐 꽉참!')
        return None
    rear = (rear + 1) % SIZE
    queue[rear] = data
    print('들어온사람 ->', queue[rear])
    print('출구 <-', queue, '<- 입구')

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty() == True:
        print('큐 텅빔!')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    print('나간사람 ->', data)
    print('출구 <-', queue, '<- 입구')
    

def peek(): # 다음 나갈 사람 리턴하는 함수
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐 텅빔!')
        return None
    print('다음 나갈 사람은 ->', queue[front+1])
    return queue[(front+1) % SIZE]


## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = 0,0


## Main
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('사나')
enQueue('나연')

peek()

deQueue()
deQueue()

enQueue('다현')
enQueue('미나')
enQueue('쯔위')
enQueue('모모')

deQueue()

peek()
