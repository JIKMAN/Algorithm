# kakao 2021 인턴쉽 1. 숫자 문자열과 영단어

'''
1478 → “one4seveneight”
234567 → “23four5six7”
10203 → “1zerotwozero3”
네오와 프로도가 위와 같이 숫자를 문자열로 바꾸는 게임을 하고 있습니다. 이때 일부 자릿수가 영단어로 바뀌었거나 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어질 때, s가 의미하는 원래 숫자를 return 하는 함수를 완성해 주세요.

제한사항
1 ≤ s의 길이 ≤ 50
s가 “zero” 또는 “0”으로 시작하는 경우는 주어지지 않습니다.
return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.
'''

dic = {'zero' : '0',
       'one' : '1',
       'two' : '2',
       'three': '3',
       'four' : '4',
       'five' : '5',
       'six' : '6',
       'seven' : '7',
       'eight' : '8',
       'nine' : '9'}

s = "2three45sixseven"

def solution(s):
    result = ""
    while len(s) > 0:
        if s[0].isdigit() == True:
            result += s[0]
            s = s[1:]
        else:
            for d in dic:
                if s.startswith(d):
                    result += dic[d]
                    s = s[len(d):]
    return int(result)

print(solution(s))


## 다른 사람의 풀이

def another_solution(s):
    result = s
    for key, value in dic.items():
        result = result.replace(key, value)
    return int(result)

print(another_solution(s))