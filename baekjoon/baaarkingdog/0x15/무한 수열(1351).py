n, p, q = map(int, input().split())
A = {0: 1}


def r(i):
    if A.get(i):
        return A[i]
    A[i] = A.get(i//p, r(i//p))+A.get(i//q, r(i//q))
    return A[i]


print(r(n))
