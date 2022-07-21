M = 10**7
while 1:
    try:
        x = int(input())*M
    except:
        exit()
    n, t = int(input()), 0
    A = sorted(int(input())for _ in ' '*n)
    for i in range(n):
        a = A[i]
        if a > x:
            continue
        l, r = i+1, n-1
        while r > l:
            m = (l+r)//2
            if a+A[m] > x:
                r = m-1
            elif a+A[m] < x:
                l = m+1
            else:
                t = 1
                print(f"yes {a} {A[l]}")
                break
    t or print('danger')
