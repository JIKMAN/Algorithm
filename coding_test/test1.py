# My_solution
import math

def solution(p, s):
    day = math.ceil((100 - p[0]) // s[0])
    count = 1
    answer = []
    for i in range(1, len(p)):
        if math.ceil((100 - p[i]) // s[i]) > day:
            if i == len(p)-1:
                answer.append(count)
                answer.append(1)
            else:                
                answer.append(count)
                count = 1
                day = math.ceil((100 - p[i]) // s[i])
        else:
            if i == len(p)-1:
                count += 1
                answer.append(count)
            else:
                count += 1
            
    return answer


progresses = [93,30,55]
speeds = [1,30,5]

print(solution(progresses, speeds))

# other solution
#  
# def solution(progresses, speeds):
#     Q = []
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0] < -((p-100)//s):
#             Q.append([-((p-100)//s), 1])
#         else:
#             Q[-1][1] +=1
#     return [q[1] for q in Q]

    
