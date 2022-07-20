while 1:
    try:
        n = int(input())
    except:
        exit()
    A = [*map(int, input().split())]
    D = []
    for a in A:
        l, r = 0, len(D)-1
        while l <= r:
            m = (l+r)//2
            if D[m] < a:
                l = m+1
            else:
                r = m-1
        if l == len(D):
            D += a,
        D[l] = a
    print(len(D))
