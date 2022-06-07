M = 8**8
n = int(input())
E = [[*map(int, input().split())]for _ in ' '*n]
b = c = 0
V = [M]*(1 << n)
for i in input()[::-1]:
    b <<= 1
    if i == 'Y':
        c += 1
        b |= 1
p = int(input())


def f(a, v, c):
    if c >= p:
        V[v] = 0
    elif not V[v]-M:
        for i in range(n):
            if v & 1 << i:
                for j in range(n):
                    if not v & 1 << j:
                        V[v] = min(V[v], f(a, v | 1 << j, c+1)+E[i][j])
                return V[v]


f(0, b, c)
print(-(V[b] == M) or V[b])
