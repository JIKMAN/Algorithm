## exam1([('John',200), ('Danial',100),('Charles',50)],'George',150)

## [('John',200),('George', 150), ('Danial',100),('Charles',50)]

def exam1(arr, name, score):
    arr.append((name, score))
    return sorted(arr, key=lambda x: x[1], reverse=True)
    


# print(exam1([('John',200), ('Danial',100),('Charles',50)], 'Kim', 10))
# print(exam1([('John',200), ('Danial',100),('Charles',50)],'George',150))

def exam2(arr):
    cnt = 0
    for idx in range(len(arr)):
        min = idx
        for j in range(idx, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if min != idx:
            arr[idx], arr[min] = arr[min], arr[idx]
            cnt += 1
    return cnt

            

print(exam2([20,12,10,15,2]))

