## 함수
def findMinIndex(ary):
    minIdx = 0
    for i in range(1, len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx



## 변수
# testAry = [55, 88, 33, 77, 66, 22]
import random
before = [random.randint(100,999) for _ in range(20)]
after = []
## Main
print('정렬전 : ', before)
for i in range(len(before)):
    min = findMinIndex(before)
    after.append(before[min])
    del(before[min])


print('정렬후 : ', after)

