n, m = map(int, input().split())


def s(n, m):
    if n == 2:
        return (1, 1) if m == 0 else (1, 2) if m == 1 else (2, 2) if m == 2 else (2, 1)
    k = n/2
    p = m / (k*k)
    a, b = s(n >> 1, m % (k*k))
    return (b, a) if p == 0 else (a, b+k) if p == 1 else (a+k, b+k) if p == 2 else (k-b+1+k, k-a+1)


print(*s(n, m))

# 풀이 참고 : https://www.programmerall.com/article/9390577247/
