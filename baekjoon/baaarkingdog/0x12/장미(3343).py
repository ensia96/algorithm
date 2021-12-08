n, a, b, c, d = map(int, input().split())


def s(i, j, k):
    x, y = divmod(i, j)
    return (x+bool(y))*k


print(min(s(n, a, b), s(n-c, a, b)+d, s(n, c, d), s(n-a, c, d)+b))
