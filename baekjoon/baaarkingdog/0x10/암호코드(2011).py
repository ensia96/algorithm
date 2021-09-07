n, m = [*map(int, input())], 10**6
L, l = lambda x: n[x-1] and n[x-1]*10+n[x] <= 26, len(n)
if not n[0]:
    exit(print(0))
a = b = 1
for i in range(1, l):
    a, b = b, (a*L(i)+b*bool(n[i])) % m
print(b)
