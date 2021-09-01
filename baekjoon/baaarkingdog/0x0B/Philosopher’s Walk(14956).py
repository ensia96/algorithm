n, m = map(int, input().split())


def s(n, m):
    if n == 2:
        return ((1, 1), (1, 2), (2, 2), (2, 1))[m]
    k = n//2
    p = m // (k*k)
    a, b = s(n//2, m % (k*k))
    return ((b, a), (a, b+k), (a+k, b+k), (k-b+1+k, k-a+1))[p]


print(*s(n, m-1))

# 풀이 참고 : https://www.programmerall.com/article/9390577247/
