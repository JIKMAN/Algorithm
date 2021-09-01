import re
from itertools import permutations, combinations, product

'''
이벤트 응모자 아이디 목록이 담긴 배열 user_id와 불량 사용자 아이디 목록이 담긴 배열 banned_id가 매개변수로 주어질 때, 당첨에서 제외되어야 할 제재 아이디 목록은 몇가지 경우의 수가 가능한 지 return 하도록 solution 함수를 완성해주세요.

[제한사항]
user_id 배열의 크기는 1 이상 8 이하입니다.
user_id 배열 각 원소들의 값은 길이가 1 이상 8 이하인 문자열입니다.
응모한 사용자 아이디들은 서로 중복되지 않습니다.
응모한 사용자 아이디는 알파벳 소문자와 숫자로만으로 구성되어 있습니다.
banned_id 배열의 크기는 1 이상 user_id 배열의 크기 이하입니다.
banned_id 배열 각 원소들의 값은 길이가 1 이상 8 이하인 문자열입니다.
불량 사용자 아이디는 알파벳 소문자와 숫자, 가리기 위한 문자 '*' 로만 이루어져 있습니다.
불량 사용자 아이디는 '*' 문자를 하나 이상 포함하고 있습니다.
불량 사용자 아이디 하나는 응모자 아이디 중 하나에 해당하고 같은 응모자 아이디가 중복해서 제재 아이디 목록에 들어가는 경우는 없습니다.
제재 아이디 목록들을 구했을 때 아이디들이 나열된 순서와 관계없이 아이디 목록의 내용이 동일하다면 같은 것으로 처리하여 하나로 세면 됩니다.
'''

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

# def solution(user_id, banned_id):
#     ban_list = []
#     for b in banned_id:
#         b = b.replace('*', '.')
#         tmp = []
#         for u in user_id:
#             if re.match(rf"{b}", u) and len(u) == len(b):
#                 tmp.append(u)
#         ban_list.append(tmp)



#     new_array = []
#     for l in list(product(*ban_list)):
#         if len(set(l)) == len(banned_id):
#             new_array.append(list(set(l)))

#     result = []
#     for n in new_array:
#         if n not in result:
#             result.append(n)

#     return len(result)

# print(solution(user_id, banned_id))
    

def solution(user_id, banned_id):
    answer = []
    candidates = [[]]
    for b_id in banned_id:
        new_candidates = []
        for u_id in user_id:
            if len(u_id) != len(b_id):
                continue
            check = True
            for i in range(len(u_id)):
                if b_id[i] != '*' and u_id[i] != b_id[i]:
                    check = False
                    break
            if check:
                for c in candidates:
                    if u_id not in c:
                        new_candidates.append(c+[u_id])
        candidates = new_candidates
    for c in candidates:
        if set(c) not in answer:
            answer.append(set(c))

    return len(answer)