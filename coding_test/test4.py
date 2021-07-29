'''
clothes의 서로다른 조합의 수를 return 하는 함수
ex)
얼굴	(동그란 안경, 검정 선글라스)
상의	(파란색 티셔츠)
하의	(청바지)
겉옷	(긴 코트)
'''
def solution(clothes):
    closet = {}
    for i in clothes:
        closet[i[1]] = 1
        
    for c, t in clothes:
        if t in closet:
            closet[t] += 1
    
    base = 1
    for v in closet.values():
        base *= v
    return base -1


clothes_1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes_2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]