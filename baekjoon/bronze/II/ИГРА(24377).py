A = *map(int, input().split()), 0
x = {1, 2, 3, 4} - {*A}
print(*[A[:2], [A.index(0) + 1, *x], x][len(x)])
