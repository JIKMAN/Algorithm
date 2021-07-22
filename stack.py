## 함수
def isStackFull() : # 스택 꽉 찼는지 확인
    global SIZE, stack, top
    if top == SIZE-1 :
        return True
    else :
        return False

def push(data) : # 푸쉬
    global SIZE, stack, top
    if isStackFull() == True :
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

def isStackEmpty() : # 스택이 비었는지 확인
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False

def pop(): # 팝
    global SIZE, stack, top
    if isStackEmpty() == True:
        print('스택 비었음!')
        return None
    data = stack[top]
    stack[top] = None
    top -=1
    return data
    
def peek() : # 다음 확인만!
    global SIZE, stack, top
    if(isStackEmpty()):
        print('스택 비었음')
        return None
    return stack[top]



## 전역
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

## 메인
push('커피');push('녹차')
push('쥬스');push('소주')

print( '바닥 |', stack)

reData = peek()
print(f'다음에 나올 것 -> {reData}')
reData = pop()
print(f'빼낸 것 -> {reData}')

reData = pop()
print(f'빼낸 것 -> {reData}')

print( '바닥 |', stack)