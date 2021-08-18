# programmers-기능개발
import math

progresses = [93, 30, 55]
speed = [1, 30, 5]

Q =[]

for p, s in zip(progresses, speed):
    if len(Q) == 0 or math.ceil((100 - p) / s) > Q[-1][0]:
        Q.append([math.ceil((100 - p) / s), 1])
    else:
        Q[-1][1] += 1
print([q[1] for q in Q])
