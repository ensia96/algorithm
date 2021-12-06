n, k, l = map(int, input().split())
L = [0]*n
L[k-1] = L[l-1] = 1
c = 0
while 1:
    L, c = [L[i]+((i+1 < n) and L[i+1])for i in range(0, n, 2)], c+1
    n = len(L)
    max(L) == 2 and exit(print(c))
