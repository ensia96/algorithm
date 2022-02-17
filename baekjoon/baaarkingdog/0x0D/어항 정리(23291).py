L, A, R = lambda: map(int, input().split()), 1, range
n, k = L()
L = [*L()]


def roll_fishbowl_array(L):
    n, t = max(i+1 for i in R(len(L[0]))if L[0][i]), []
    if len(L[0])-n < len(L):
        return L
    for i in R(len(L))[::-1]:
        t += [L[i][:n]]
        L[i] = L[i][n:]
    return roll_fishbowl_array([[*t]+[0]*(len(L[-1])-len(t))for t in [*zip(*t)]]+[L[-1]])


def control_fish_count():
    r, c = len(L), len(L[0])
    T = [[0]*c for _ in ' '*r]
    X = [(i, j)for i in R(r)for j in R(c)]
    for i, j in X:
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < r and 0 <= y < c and L[x][y]:
                t = (L[i][j]-L[x][y])//5
                if t > 0:
                    T[i][j] -= t
                    T[x][y] += t
    for i, j in X:
        L[i][j] += T[i][j]


def serialize_fishbowl_array():
    n, m = len(L), len(L[0])
    return [L[i][j]for j in R(m)for i in R(n)[::-1]if L[i][j]]


def fold_fishbowl_array(L, d=0):
    if type(L[0]) != list:
        L = [L]
    n = len(L[0])//2
    if d == 2:
        return L
    t = []
    for l in L[::-1]:
        t += [l[:n][::-1]]
    for l in L:
        t += [l[n:]]
    return fold_fishbowl_array(t, d+1)


while A:
    t = min(L)
    L = [l+(l == t)for l in L]
    L = [[L[0]]+[0]*(n-2), L[1:]]
    L = roll_fishbowl_array(L)
    control_fish_count()
    L = serialize_fishbowl_array()
    L = fold_fishbowl_array(L)
    control_fish_count()
    L = serialize_fishbowl_array()
    if max(L)-min(L) <= k:
        break
    A += 1
print(A)
