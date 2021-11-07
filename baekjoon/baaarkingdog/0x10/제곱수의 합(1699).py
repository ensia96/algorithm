n = int(input())
c, d = 0, [i**2 for i in range(318)]
while 1:
    for i in range(318):
        if d[i] > n:
            n, c = n-d[i-1], c+1
            break
    if n == 0:
        exit(print(c))
