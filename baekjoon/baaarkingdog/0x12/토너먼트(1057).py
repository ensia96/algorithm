n, k, l, c = *map(int, input().split()), 0
while k != l:
    k, l, c = k-k//2, l-l//2, c+1
print(c)
