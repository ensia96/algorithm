a, b, c, d = '|-* '
n = int(input())
print(a + b * (n - 2) + a)
for i in range(1, n - 1):
    l = [d] * n
    l[0] = a
    l[-1] = a
    l[i] = c
    l[-i - 1] = c
    print(''.join(l))
print(a + b * (n - 2) + a)
