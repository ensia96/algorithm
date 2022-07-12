import sys
I = sys.stdin.readline
for _ in ' '*int(I()):
    n, A = int(I()), sorted(map(int, I().split()))
    I()
    for i in map(int, I().split()):
        t, l, r = 0, 0, n-1
        while l <= r:
            m = (l+r)//2
            if A[m] > i:
                r = m-1
            else:
                l, t = m+1, m
        print(+(A[t] == i))
