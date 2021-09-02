def b(n, m, l=[]):
    if len(l) == m:
        print(*map(str, l))
    for i in range(1, n+1):
        if i not in l:
            b(n, m, l + [i])


b(*map(int, input().split()))
