while 1:
    n, *H = map(int, input().split())
    if not n:
        break
    S = []
    A = min(H)*n
    H = [0]+H
    while H:
        h, w = H.pop(), 1
        while S and S[-1][0] >= h:
            a, b = S.pop()
            w += b
            A = max(A, a*(w-1))
        S += (h, w),
        A = max(A, h*w)
    print(A)
