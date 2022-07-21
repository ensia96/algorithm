M = 10**7
while 1:
    try:
        x = int(input())*M
    except:
        exit()
    n, T, t = int(input()), [], 'danger'
    A = sorted(int(input())for _ in ' '*n)
    for i in range(n):
        a = A[i]
        if a > x:
            continue
        l, r = i+1, n-1
        while r > l:
            m = (l+r)//2
            if a+A[m] < x:
                l = m+1
            else:
                r = m-1
        if l < n and a+A[l] == x:
            t = f"yes {a} {A[l]}"
            break
    print(t)
