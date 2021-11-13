## 1
# 배열에 포함된 가장 큰 홀수 + 가장 큰 짝수

array = [5,3,10,6,11]

array = sorted(array, reverse=True)

answer = 0
r1 = []
r2 = []
for i in array:
    if i % 2 == 0:
        r1.append(i)
    else:
        r2.append(i)

if r1:
    answer += max(r1)
if r2:
    answer += max(r2)
print(answer)


## 2
# 같은 알파벳의 집합으로 나눈 후
# 모든 집합을 가장 긴 집합의 길이로 만드는 데 추가해야되는 알파벳 수

S = 'abaabbccc' # 가장 긴 집합 ccc : a -> aaa, b -> bbb, aa -> aaa, bb -> bbb

def solution(S):
    new = []
    tmp = S[0]
    now = S[0]
    for i in range(1, len(S)):
        if S[i] != now:
            new.append(tmp)
            tmp = S[i]
            now = S[i]
        else:
            tmp += S[i]
    if tmp:
        new.append(tmp)

    max_leng = len(max(new, key=len))

    cnt = 0
    for w in new:
        while len(w) < max_leng:
            w += w[0]
            cnt += 1
    return cnt

print(solution(S))


## 3
# 1 -> 1 번 나오거나 0번 나오도록
# 2 -> 2 번 나오거나 0번 나오도록
# ...
# 8 -> 8 번 나오거나 0번 나오도록
# 로 만드는데 추가하거나 빼야하는 연산의 수

def solution(array):
    max_num = array[-1]

    answer = 0
    for i in range(1, max_num + 1):
        tmp = []
        for k in array:
            if k == i:
                tmp.append(k)
        if tmp:
            answer += min(abs(len(tmp) - i), len(tmp))
        array = array[len(tmp):]
        

    return answer



A = [1,1,3,3,4,4,4]
print(solution(A))
A = [1,2,2,2,5,5,5,8]
print(solution(A))
A = [1,1,1,1,3,3,4,4,4,4,4]
print(solution(A))