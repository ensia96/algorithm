def solution(cap, n, deliveries, pickups):
    D = [i for i in range(n)if deliveries[i]]
    P = [i for i in range(n)if pickups[i]]
    A = 0
    while D or P:
        j = 0
        if D:
            x = 0
            j = max(j, D[-1])
            while D:
                i = D.pop()
                if x+deliveries[i] > cap:
                    y = cap-x
                    deliveries[i] -= y
                    x += y
                    D += i,
                    break
                else:
                    x += deliveries[i]
                    deliveries[i] = 0
        if P:
            x = 0
            j = max(j, P[-1])
            while P:
                i = P.pop()
                if x+pickups[i] > cap:
                    y = cap-x
                    pickups[i] -= y
                    x += y
                    P += i,
                    break
                else:
                    x += pickups[i]
                    pickups[i] = 0
        A += j+1
    return A*2

# 가장 먼 곳부터 다녀오면서 오는 길에 이것저것 처리하면 됨
# -> 틀림..
# -> 약간 그리디 느낌 나는데..
# -> 그냥 구현 실수한 부분 찾아서 고침


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
# 16
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
# 30
