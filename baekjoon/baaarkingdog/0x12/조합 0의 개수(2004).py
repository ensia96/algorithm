n, m = map(int, input().split())


def f(x, f):
    y = 0
    while x//f:
        x, y = x//f, y+x//f
    return y


print(min(f(n, i)-f(n-m, i)-f(m, i) for i in [2, 5]))
