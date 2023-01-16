d, h, m = map(int, input().split())
A = 60*(24*d+h)+m-16511
print(-1 if A < 0 else A)
