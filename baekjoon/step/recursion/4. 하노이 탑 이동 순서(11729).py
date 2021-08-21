n = int(input())
x = sum(2 ** _ for _ in range(n))
t = [[21, *(i for i in range(n, 0, -1))], [21], [21]]
r = [[21], [21], list(t[0])]


def m(t, s, g):
    return (
        not (t[g].append(t[s].pop()))
        if t[s] and t[g] and t[s][-1] < t[g][-1]
        else False
    )


def s(a=[]):
    if len(a) > x:
        return False
    if t == r:
        return a

    for i in range(3):
        for j in range(3):
            if i != j and m(t, i, j):
                a.append((f"{i + 1} {j + 1}"))
                if s(a):
                    return a
                else:
                    a.pop()
                    m(t, j, i)


print(x)
print("\n".join(s()))


# 1
# 1 3

# 3
# 1 2
# 1 3
# 2 3

# 7
# 1 3 | 3 1
# 1 2 | 3 2
# 3 2 | 1 2
# 1 3 | 3 1
# 2 1 | 2 3
# 2 3 | 2 1
# 1 3 | 3 1

# 15
# 1 2
# 1 3
# 2 3
# 1 2
# 3 1
# 3 2
# 1 2
# 1 3
# 2 3
# 2 1
# 3 1
# 2 3
# 1 2
# 1 3
# 2 3

[
    (1, 2),
    (1, 3),
    (2, 3),
    (1, 2),
    (3, 1),
    (3, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (2, 1),
    (3, 1),
    (2, 3),
    (1, 2),
    (1, 3),
    (2, 3),
]
