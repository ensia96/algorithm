n, m, *A = map(int, open(0).read().split())
print(A[:n].index(min(A[:n])) + 1, A[-m:].index(min(A[-m:])) + 1)
