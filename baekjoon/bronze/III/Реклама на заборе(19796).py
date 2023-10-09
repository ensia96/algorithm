m, n = map(int, input().split())
T = [0]*m
for _ in ' '*n:
    a, b = map(int, input().split())
    for i in range(a-1, b):
        T[i] = 1
print('YNEOS'[sum(T) != m::2])
