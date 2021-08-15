def solution(scores):
    answer = ""
    for i in range(len(scores[0])):
        tmp = []
        for j in range(len(scores)):
            tmp.append(scores[j][i])
        if (tmp[i] == max(tmp) and tmp.count(tmp[i]) < 2) or (tmp[i] == min(tmp) and tmp.count(tmp[i]) < 2):
            tmp.remove(tmp[i])
        avg = (sum(tmp) / len(tmp))
        if avg >= 90:
            answer += "A"
        elif avg >= 80:
            answer += "B"
        elif avg >= 70:
            answer += "C"
        elif avg >= 50:
            answer += "D"
        else:
            answer += "F"
    return answer


scores = [[100,90,98,88,65],
          [50,45,99,85,77],
          [47,88,95,80,67],
          [61,57,100,80,65],
          [24,90,94,75,65]]

print(solution(scores))

