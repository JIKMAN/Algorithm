# stack = [None, None, None, None, None]
# top = -1 # 위치 설정

# # 삽입(Push) 구현
# top += 1
# stack[top] = '커피'
# top += 1
# stack[top] = '녹차'
# print(stack)

# # 추출(Pop) 구현
# data = stack[top]
# stack[top] = None
# top -= 1
# print('추출 -> ', data)
# print(stack)

# data = stack[top]
# stack[top] = None
# top -= 1
# print('추출 -> ', data)
# print(stack)



SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

def isStackFull(): # 스택이 꽉 찼는지 확인하는 함수
    global SIZE, stack, top
    if top == SIZE-1:
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if isStackFull() == True:
        print('Stacked Full!')
        return
    top += 1
    stack[top] = data

push('커피')
push('녹차')
push('꿀물')
print(stack)