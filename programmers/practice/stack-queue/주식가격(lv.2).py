def solution(prices):
    '''
    input
        - prices : [주식가격] (2 <= [] <= 100000, 1 <= i <= 10000)
    output
        - answer : 각 시점마다 주식이 떨어지지 않은 기간
    '''
    from itertools import islice
    answer = []
    time   = 0

    for current, price in enumerate(prices):
        pass

    return answer

print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
