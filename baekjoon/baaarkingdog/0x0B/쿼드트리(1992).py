import sys
i, r = sys.stdin.readline, range
n = int(i())
m = [[*map(int, [*i().strip()])] for _ in r(n)]


def q(n, x=0, y=0, l=[[], [], [], []]):
    if n == 1:
        return m[x][y]
    n, t = n // 2, [[], [], [], []]
    for i, a, b in [(0, x, y), (1, x, y+n), (2, x+n, y), (3, x+n, y+n)]:
        c = q(n, a, b, t[i])
        t[i] = c if n else m[x][y]
    t = 1 if len([*filter(lambda x: x == 1, t)]
                 ) == 4 else 0 if not any(t) else t
    return t


print(str(q(n)).replace('[', '(').replace(', ', '').replace(']', ')'))
