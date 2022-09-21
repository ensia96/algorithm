a, b = map(int, input().split())
Q, c = [a], 0
while Q:
    q = []
    for i in Q:
        if i == b:
            exit(print(c+1))
        for j in [i*2, 10*i+1]:
            if j <= b:
                q += j,
    Q = q
    c += 1
print(-1)
