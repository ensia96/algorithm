M = 10**7
while 1:
    try:
        x = int(input())*M
    except:
        exit()
    n, t = int(input()), 0
    A = sorted(int(input())for _ in ' '*n)
    l, r = 0, n-1
    while l < r:
        y = A[l]+A[r]
        if y > x:
            r -= 1
        elif y < x:
            l += 1
        else:
            t = 1
            print(f"yes {A[l]} {A[r]}")
            break
    t or print('danger')
