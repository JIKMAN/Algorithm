## 함수
def binSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary)-1

    while start <= end:
        mid = (start + end) // 2
        if fData == ary[mid]:
            return mid
        elif fData > ary[mid]:
            start = mid + 1
        else:
            end = mid -1

    return pos # 찾는 데이터가 없으면 -1 리턴


## 변수
dataAry = [50, 60, 105, 120, 150, 160, 170, 180, 190, 191] # 주어진 배열
findData = 160 # 찾아야되는 키



## Main
print(dataAry)
position = binSearch(dataAry, findData)
if position == -1:
    print('없다.')

else:
    print(findData,'->', position, '번 위치에 있음')