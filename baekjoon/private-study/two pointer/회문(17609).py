def f(l, r, c):
    if l >= r:
        return c
    if A[l] == A[r]:
        return f(l+1, r-1, c)
    elif not c:
        return min(f(l+1, r, 1), f(l, r-1, 1))
    else:
        return 2


for _ in ' '*int(input()):
    A = input()
    print(f(0, len(A)-1, 0))
