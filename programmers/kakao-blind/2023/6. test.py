import sys
sys.setrecursionlimit(10**6)

N = M = R = C = K = 0
A = []
D = {'d': (1, 0), 'l': (0, -1), 'r': (0, 1), 'u': (-1, 0)}


def f(x, y, r):
    if abs(x-R)+abs(y-C)+len(r) > K:
        return if (x, y) == (R, C) and len(r) == K:
        A.append(r)
        return
    for k in sorted(D):
        p, q = D[k]
        i, j = x+p, y+q
        if 0 <= i < N and M > j >= 0:
            f(i, j, r+k)


def solution(n, m, x, y, r, c, k):
    global N, M, R, C, K
    N, M, R, C, K = n, m, r-1, c-1, k
    f(x-1, y-1, '')
    return sorted(A)[0] if A else 'impossible'


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))

# 그냥 너비 우선 탐색 + 완전 탐색으로 구현
# -> 시간 초과 + 런타임 에러..
# -> 재귀 제한 풀어봄
# -> 일단 런타임 에러는 사라짐..
# -> 목적지까지의 거리를 기준으로 재귀 깊이를 조절하도록 수정해봄
# -> 그래도 시간 초과..
# -> 나중에 해설 꼭 봐바야 할 듯;
# -> 일부 케이스는 맞음
# -> 사실 4**k 풀이라서 답이 없긴 했음;
