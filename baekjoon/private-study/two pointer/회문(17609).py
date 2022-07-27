for _ in ' '*int(input()):
    A = input()
    c, l, r = 0, 0, len(A)-1
    while l < r and c < 2:
        if A[l] != A[r]:
            c += 1
            if A[l+1] == A[r]:
                l += 1
            elif A[l] == A[r-1]:
                r -= 1
            else:
                c = 2
                break
        l += 1
        r -= 1
    print(c)
