n, k = map(int, input().split())
l, c = [*range(n+1)], 0
for i in range(2, n+1):
    for j in range(i, n+1, i):
        if not l[j]:
            continue
        l[j], c = 0, c+1
        if c == k:
            exit(print(j))
