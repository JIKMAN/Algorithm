def solution(n):
    result = 0
    for i in range(1, n):
        result += (n * i) + i
    
    return result


print(solution(5))