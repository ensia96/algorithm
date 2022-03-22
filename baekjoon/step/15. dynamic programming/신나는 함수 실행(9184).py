M = 8**8


def w(a, b, c):
    if min(a, b, c) <= 0:
        a = b = c = 0
    if max(a, b, c) > 20:
        a = b = c = 20
    if T[a][b][c] != M:
        return T[a][b][c]
    f = (a < b)*(b < c)
    F = not f
    T[a][b][c] = w(a-F, b, c-f)+w(a-F, b-1, c-f) - \
        w(a-F, b-1, c-F)+w(a-1, b, c-1)*F
    return T[a][b][c]


while 1:
    a, b, c = map(int, input().split())
    if (a == -1)*(b == -1)*(c == -1):
        break
    T = [[[M]*21 for _ in ' '*21]for _ in ' '*21]
    T[0][0][0] = 1
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
