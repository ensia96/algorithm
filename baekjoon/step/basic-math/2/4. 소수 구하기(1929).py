m, n = map(int, input().split())

for i in range(m, n + 1):
    a = 1
    for j in range(2, i):
        if not i % j:
            a = 0
            break
    if a:
        print(i)
