# 문제수가 5 이상, 푼 문제수가 같다.
# 푼 문제의 번호가 모두 같다.
# 푼 문제의 점수가 모두 같다.

# 수험번호, 문제 번호, 받은 점수
# 없을 경우 None
logs = ["0001 3 95", 
"0001 5 90", 
"0001 5 100", 
"0002 3 95", 
"0001 7 80", 
"0001 8 80", 
"0001 10 90", 
"0002 10 90", 
"0002 7 80", 
"0002 8 80", 
"0002 5 100", 
"0003 99 90"]

from collections import defaultdict


def solution(logs):
    tester = defaultdict()

    solve = defaultdict(int)

    id = set()
    for i in range(len(logs)):
        logs[i] = logs[i].split(" ")
        tester[logs[i][0]] = [0 for _ in range(101)]
        id.add(logs[i][0])
        solve[logs[i][0]] += 1

    for a,b,c in logs:
        if tester[a][int(b)] != 0:
            tester[a][int(b)] = max(tester[a][int(b)], int(c))
        else:
            tester[a][int(b)] = int(c)
    id = list(id)

    result = []
    for i in range(len(id)-1):
        for j in range(i+1, len(id)):
            if solve[id[i]] < 5 or solve[id[j]] < 5:
                continue
            if tester[id[i]] == tester[id[j]]:
                result.append(id[i])
                result.append(id[j])
    if result is None:
        return None
    return sorted(set(result))


print(solution(logs))

