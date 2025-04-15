from itertools import product


def solution(users, emoticons):
    n = len(users)
    m = len(emoticons)
    A = B = 0
    for P in product([90, 80, 70, 60], repeat=m):
        E = [emoticons[i]*P[i]//100 for i in range(m)]
        x = y = 0
        for i in range(n):
            s, p = users[i]
            S = sum(E[j]for j in range(m)if 100-P[j] >= s)
            if S >= p:
                x += 1
            else:
                y += S
        if x > A:
            A, B = x, y
        elif x == A:
            B = max(B, y)
    return [A, B]


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
# [1, 5400]
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [
      40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
# [4, 13860]

# 이 문제도 그리디같음..
# -> 구독자 수가 최대이면서 판매 가격도 최대가 되는 할인율을 찾아야 함
# -> 기준보다 높은 할인율은 무조건 구매
# -> 총 구매 비용이 기준을 넘어가면 구독함
# -> n, m 크기가 작은거로 봐서는 완전 탐색 문제인듯
# -> m <= 7 이고, 적용 가능한 할인율은 4가지, 총 사용자 수는 100명 = 4**7 * 100 * 7 = 11468800
