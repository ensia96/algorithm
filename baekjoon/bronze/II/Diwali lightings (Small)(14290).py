_, *A = open(i := 0)
while A:
    s, n, *A = A
    a, b = map(int, n.split())
    i += 1
    print(f'Case #{i}:', (s[:-1] * b)[a - 1:b].count('B'))
