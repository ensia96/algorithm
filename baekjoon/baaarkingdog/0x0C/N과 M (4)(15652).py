def b(n, m, l=[]):
    if len(l) == m:
        print(*map(str, l))
        return
    for i in range(1, n+1):
        if not l or l[-1] <= i:
            b(n, m, l+[i])


b(*map(int, input().split()))
