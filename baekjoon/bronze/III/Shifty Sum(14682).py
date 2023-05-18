a, b = map(int, [*open(0)])
print(sum(a*10**i for i in range(b+1)))
