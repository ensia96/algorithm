x, m = map(int, open(0))
print(*[i for i in range(m)if x*i % m == 1] or ["No such integer exists."])
