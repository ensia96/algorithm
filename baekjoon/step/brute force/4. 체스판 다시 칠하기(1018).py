def e(l):
    a = sum(
        (((i + j) % 2) + int("W" == l[i][j])) % 2 for i in range(8) for j in range(8)
    )

    return min(a, 64 - a)


m, n = map(int, input().split())
b = [input() for _ in range(m)]

print(
    min(
        e([l[j : j + 8] for l in b[i : i + 8]])
        for j in range(n - 7)
        for i in range(m - 7)
    )
)
