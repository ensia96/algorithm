n = int(input())
a, b = map(int, input().split())
m = int(input())
A = [~-int(input())for _ in ' '*m]


def f(x, y, z):
    if z == m:
        return 0
    return min(abs(x-A[z])+f(A[z], y, z+1), abs(y-A[z])+f(x, A[z], z+1))


print(f(a-1, b-1, 0))
