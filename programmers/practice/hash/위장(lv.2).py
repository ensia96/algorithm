def solution(clothes):
    '''
    input
        - clothes : [[의상 이름, 의상 종류]] (1 <= [] <= 30, 1 <= i <= 20)
    output
        - answer  : 서로 다른 옷의 조합의 수
    result
        - 정확성 : 100/100
    '''
    test = {}

    for name, kind in clothes:
        if kind not in test:
            test[kind] = []
        test[kind].append(name)

    _test = 1

    for key in test:
        _test *= len(test[key]) + 1

    return _test - 1

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
