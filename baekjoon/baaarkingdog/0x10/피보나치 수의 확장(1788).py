N = int(input())
n, f = abs(N), N >= 0
a, b, c, d = *[0, 1][::f or -1], n, 10**9
for i in range(2, n+2-f):
    c = [a-b, a+b][f]
    c = [c % d, -(-c % d)][c < 0]
    a, b = b, c
print(int(c > 0 or (c < 0)*-1))
print(abs(c))
