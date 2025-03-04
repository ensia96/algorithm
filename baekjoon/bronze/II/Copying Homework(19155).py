_, *A = map(int, open(0).read().split())
print(*[1 - a + _ for a in A])
