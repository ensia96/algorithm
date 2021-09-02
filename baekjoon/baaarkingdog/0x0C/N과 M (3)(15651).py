def b(n, m, l=[]):
    if len(l) == m:
        print(*map(str, l))
        return
    for i in range(1, n+1):
        b(n, m, l+[i])


b(*map(int, input().split()))
