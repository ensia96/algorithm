n, *L = map(int, open(0).read().split())
for i in range(n):
    A = []
    for j in range(3):
        x, y = divmod(sum(L[30*i+j:30*i+30+j:3]), 10)
        A += x+(y > 4),
    print(*A)
