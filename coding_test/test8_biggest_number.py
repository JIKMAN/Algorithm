# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꿔주는 함수

def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(reverse=True, key=lambda x: x*3)
    return ''.join(numbers)

numbers = [6, 10, 2, 13, 34]

print(solution(numbers))

