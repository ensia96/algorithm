def f(l, r, c):
    while l < r:
        if A[l] == A[r]:
            l += 1
            r -= 1
        elif not c:
            return 1+(f(l+1, r, 1)-1)*(f(l, r-1, 1)-1)
        else:
            return 2
    return c


for _ in ' '*int(input()):
    A = input()
    print(f(0, len(A)-1, 0))
