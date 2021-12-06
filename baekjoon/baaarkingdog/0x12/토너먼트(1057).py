n, k, l = map(int, input().split())
k, l, c = k-1, l-1, 1
while 1:
    if k-l in [1, -1]:
        exit(print(c))
    k, l, c = k//2, l//2, c+1
