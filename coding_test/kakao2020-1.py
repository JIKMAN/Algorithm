# kakao2020
# 괄호 변환
'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
4-3. ')'를 다시 붙입니다. 
4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
4-5. 생성된 문자열을 반환합니다.'''

p = "(()())()"
p2 = "()))((()"

# 분리하는 함수
# w를 u와 v로 나눈다. 나눌 수 없으면 그대로 w를 반환
def devide(w):
    open = 0
    close = 0
    for i in range(len(w)):
        if w[i] == "(":
            open += 1 
        elif w[i] == ")":
            close += 1
        if open == close:
            return w[:i+1], w[i+1:]
    return w

# u가 올바른 괄호 문자열인지 확인하는 함수
def isbalance(u):
    stack = []
    
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    # 1
    if p == "":
        return p
    # 2
    u, v = devide(p)
    # 3
    if isbalance(u) == True:
        return u + solution(v)
    # 4
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
    for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
    return answer

print(solution(p))
print(solution(p2))






            

