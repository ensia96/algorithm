input()
A, D = [], {}


def f(S):
    T = D
    for s in S:
        T[s] = T = T.get(s, {})
        if 0 in T:
            return 1
    return 0


def p(S):
    T = D
    for s in S:
        T = T[s]
    T[0] = 1


def e(x, y):
    if not y:
        p(x), A.append(x)
        return 1
    for i in '01':
        if not f(x+i) and e(x+i, y-1):
            return 1


for i in sorted(map(int, input().split())):
    e('', i) or exit(print(-1))
print(1, *A, sep='\n')
