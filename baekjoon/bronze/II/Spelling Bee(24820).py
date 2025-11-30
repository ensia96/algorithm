n, *A = open(0)
print(*[a[:-1]for a in A if 1 > len({*a} - {*n}) and 4 < len(a) and n[0] in a])
