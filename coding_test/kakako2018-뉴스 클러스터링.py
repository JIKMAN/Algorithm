# kakako2018-뉴스 클러스터링
'''
입력으로는 str1과 str2의 두 문자열이 들어온다. 각 문자열의 길이는 2 이상, 1,000 이하이다.
입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 이때 영문자로 된 글자 쌍만 유효하고, 
기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다. 예를 들어 "ab+"가 입력으로 들어오면, 
"ab"만 다중집합의 원소로 삼고, "b+"는 버린다.
다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. "AB"와 "Ab", "ab"는 같은 원소로 취급한다.
입력으로 들어온 두 문자열의 자카드 유사도를 출력한다. 유사도 값은 0에서 1 사이의 실수이므로, 
이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.
'''

## 지저분한 내 풀이

test_1_str01, test_1_str02 = 'FRANCE', 'french'
test_2_str01, test_2_str02 = 'handshake', 'shake hands'
test_3_str01, test_3_str02 = 'aa1+aa2', 'AAAA12'
test_4_str01, test_4_str02 = 'E=M*C^2',	'e=m*c^2'

from collections import Counter


def make_dic(str1):
    count_dic = {}
    tmp_list = []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() == False or str1[i+1].isalpha() == False:
            continue
        tmp_list.append(str1[i:(i+2)].upper())

    count_dic = Counter(tmp_list)
    
    return count_dic


def solution(str1, str2):
    dic1 = make_dic(str1)
    dic2 = make_dic(str2)

    whole = 0
    part = 0

    for dic in dic1:
        if dic in dic2:
            whole += max(dic1[dic], dic2[dic])
            part += min(dic1[dic], dic2[dic])
        else:
            whole += dic1[dic]
    for dic in dic2:
        if dic not in dic1:
            whole += dic2[dic]

    if part == 0 and whole == 0:
        return 65536
    else:
        return int((part / whole) * 65536)

print(solution(test_1_str01, test_1_str02))
print(solution(test_2_str01, test_2_str02))
print(solution(test_3_str01, test_3_str02))
print(solution(test_4_str01, test_4_str02))

## re 정규표현식 이용

import re

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return int((gyo_sum/hap_sum)*65536)

print(solution(test_1_str01, test_1_str02))
print(solution(test_2_str01, test_2_str02))
print(solution(test_3_str01, test_3_str02))
print(solution(test_4_str01, test_4_str02))