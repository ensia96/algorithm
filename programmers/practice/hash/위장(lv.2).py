def solution(clothes):
    '''
    input
        - clothes : [[의상 이름, 의상 종류]] (1 <= [] <= 30, 1 <= i <= 20)
    output
        - answer  : 서로 다른 옷의 조합의 수
    result
        - 정확성 : 100/100
    '''
    closet = {}

    for name, kind in clothes:
        if kind not in closet:
            closet[kind] = []
        closet[kind].append(name)

    answer = 1

    for key in closet:
        answer *= len(closet[key]) + 1

    return answer - 1

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
