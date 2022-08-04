while 1:
    n, m = map(int, input().split())
    n+m or exit()
    A, B = [int(input())for _ in ' '*n], [int(input())for _ in ' '*m]
    c = l = r = 0
    while l < n and r < m:
        if A[l] < B[r]:
            l += 1
        elif A[l] > B[r]:
            r += 1
        else:
            c += 1
            l += 1
            r += 1
    print(c)
