f, _ = lambda: map(int, input().split()), ' '
for _ in _*[*f()][0]:
    p, m = f()
    A = [0]*m
    for _ in _*p:
        A[[*f()][0]-1] |= 1
    print(p-sum(A))
