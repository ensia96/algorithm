M = 8**8
n = int(input())
E = [[*map(int, input().split())]for _ in ' '*n]
A = [i == 'Y'for i in input()]
p = int(input())
b, c = 1 << n, 0
for i in range(n):
    if A[i]:
        c += 1
        b |= 1 << i


def f(v, c):
    if c >= p:
        return 0
    t = M
    for i in range(n):
        if v & 1 << i:
            for j in range(n):
                if not v & 1 << j:
                    t = min(t, f(v | 1 << j, c+1)+E[i][j])
    return t


A = f(b, c)
print(-(A == M) or A)
