n, c = int(input()), 0
x, y, z = [1] * n, [1] * (2*n - 1), [1] * (2*n - 1)


def q(v):
    global c
    if v == n:
        c += 1
        return
    for i in range(n):
        if x[i] and y[v + i] and z[v-i+n-1]:
            a, b = v + i, v-i+n-1
            x[i], y[a], z[b] = 0, 0, 0
            q(v + 1)
            x[i], y[a], z[b] = 1, 1, 1


q(0)
print(c)
