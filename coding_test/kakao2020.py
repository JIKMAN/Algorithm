test01 = "aabbaccc"
test02 = "ababcdcdababcdcd"
test03 = "abcabcdede"
test04 = "abcabcabcabcdededededede"
test05 = "xababcdcdababcdcd"

s = "aabbaccc"

from math import ceil

def solution(s):
    answer = []

    for i in range(ceil(len(s) / 2)):
        cut = i + 1
        result = ""
        tmp = s[:cut]
        count = 1
        for j in range(cut, len(s), cut):
            
            if s[j:].startswith(tmp):
                count += 1
            else:
                if count == 1:
                    count = ""
                result += (str(count) + tmp)
                tmp = s[j:(j+cut)]
                count = 1
        if count == 1:
            count = ""
        result += (str(count) + tmp)
                
        answer.append(len(result))

    return min(answer)


print(solution(s))