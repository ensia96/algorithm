P = print
a, b, c, d = '|-* '
n = int(input())
P(x := a + b * (n - 2) + a)
for i in range(1, n - 1):
    l = [d] * n
    l[0] = l[-1] = a
    l[i] = l[~i] = c
    P(''.join(l))
P(x)
