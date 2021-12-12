import bisect as b


def p(l, a):
    T = [a[0]]
    for i in range(1, l):
        T += [T[i-1]+a[i]]
    return T+[T[i]-T[j]for i in range(l)for j in range(i)]


l, t = lambda: (int(input()), [*map(int, input().split())]), int(input())
A, B = p(*l()), sorted(p(*l()))
print(sum(b.bisect_right(B, t-a)-b.bisect_left(B, t-a)for a in A))
