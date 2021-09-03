import itertools as t
r = range
m = [input().strip() for _ in r(5)]


def c(s):
    l = [(i % 5, i//5) for i in s]
    if sum(m[y][x] == 'S' for x, y in l) < 4:
        return 0
    v, q = [0] * 7, [l[0]]
    for x, y in q:
        for i in r(7):
            a, b = l[i]
            if not v[i] and abs(a - x) + abs(b - y) == 1:
                v[i] = 1
                q += [l[i]]
    return all(v)


print(sum(c(k) for k in t.combinations(r(25), 7)))
