n, p, q = map(int, input().split())
A = {}


def r(i):
    if not i:
        return 1
    A[i] = A.get(i//p, r(i//p))+A.get(i//q, r(i//q))
    return A[i]


print(r(n))
