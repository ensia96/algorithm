def f(l, r, c):
    if l >= r or c > 1:
        return c
    if A[l] != A[r]:
        c += min(f(l+1, r, c), f(l, r-1, c), 1)+1
    else:
        c += f(l+1, r-1, c)
    return c


for _ in ' '*int(input()):
    A = input()
    print(f(0, len(A)-1, 0))
