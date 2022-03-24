import bisect as B
n = int(input())
A = [*map(int, input().split())]


def f(A):
    D, R = [1]*n, [0, A[0]]
    for i in range(1, n):
        a = A[i]
        b = B.bisect_left(R, a)
        if R[-1] < a:
            R += [a]
        else:
            R[b] = a
        D[i] = b
    return D


print(max(map(sum, zip(f(A), f(A[::-1])[::-1])))-1)
