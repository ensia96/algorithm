n = int(input())
A = [[*map(int, input().split())]for _ in ' '*n]


def f(x, y, z):
    if x == n:
        return abs(y-z)
    s, b = A[x]
    return min(f(x+1, y, z), f(x+1, y*s, z+b))


print(f(1, *A[0]))
