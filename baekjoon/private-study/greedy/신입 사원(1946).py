for _ in ' '*int(input()):
    n = int(input())
    a, *A = sorted((*map(int, input().split()),)for _ in ' '*n)
    c = 1
    for i in range(n-1):
        if a[1] > A[i][1]:
            c += 1
            a = A[i]
    print(c)
