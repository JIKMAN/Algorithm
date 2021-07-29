# number에서 가장 큰 숫자를 k개 제거한 후 가장 큰 숫자를 문자열 형태로 return
# k는 1이상 number의 자릿수 미만인 자연수
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)