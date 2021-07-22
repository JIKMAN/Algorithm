## 함수
# def isQueueFull(): # 큐가 가득 찼는지 확인하는 함수
#     global SIZE, queue, front, rear
#     if rear == SIZE-1:
#         return True
#     else:
#         return False

def isQueueFull(): # 큐가 가득 찼는지 확인 
    global SIZE, queue, front, rear
    if rear != SIZE-1: # 뒤에 여유가 있는 경우
        return False
    elif rear == SIZE-1 and front == -1: # 큐가 꽉찬 경우
        return True
    else: # 큐의 앞쪽에 자리가 비어있는 경우
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -=1
        rear -=1
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
        return
    rear +=1
    queue[rear] = data
    print('들어온사람 ->', queue[rear])
    print('출구 <-', queue, '<- 입구')

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty() == True:
        print('큐 텅빔!')
        return
    front +=1
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
    return queue[front+1]


## 전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = -1, -1


## Main
enQueue('화사')
enQueue('솔라')

peek()

deQueue()
deQueue()

enQueue('문별')
enQueue('사나')
enQueue('나연')
enQueue('세정')

deQueue()

peek()

