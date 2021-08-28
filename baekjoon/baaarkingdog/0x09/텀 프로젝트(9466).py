import sys
i, t, r = sys.stdin.readline, int, range

for _ in r(t(i())):
    n, z = t(i()), 0
    s, v = [0] + [*map(t, i().split())], [0] * (n + 1)
    for p in r(1, n + 1):
        if not v[p]:
            a = p
            while 1:
                v[a] = 1
                a = s[a]
                if v[a]:
                    if v[a] == 1:
                        if a != p:
                            while v[a] != 2:
                                v[a] = 2
                                a = s[a]
                            a = p
                            while v[a] != 2:
                                v[a] = 3
                                a = s[a]
                            break
                        else:
                            while v[a] != 2:
                                v[a] = 2
                                a = s[a]
                            break
                    else:
                        a = p
                        while v[a] == 1:
                            v[a] = 3
                            a = s[a]
                        break

    print(v.count(3))
