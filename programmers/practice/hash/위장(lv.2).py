def solution(clothes):
    '''
    input
        - clothes : [[의상 이름, 의상 종류]] (1 <= [] <= 30, 1 <= i <= 20)
    output
        - answer  : 서로 다른 옷의 조합의 수
    '''
    closet = {}

    for name, kind in clothes:
        closet[name] = kind

    answer = 0
    return answer

print(solution([
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"]
])) # 5
print(solution([
    ["crowmask", "face"],
    ["bluesunglasses", "face"],
    ["smoky_makeup", "face"]
])) # 3
