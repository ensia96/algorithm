n, m = [*map(int, input())], 10**6
L, l = lambda x: n[x-1] and n[x-1]*10+n[x] <= 26, len(n)
if not n[0]:
    exit(print(0))
D = [1]*l
for i in range(1, l):
    D[i] = (D[i-2]*L(i)+D[i-1]*bool(n[i])) % m
print(D[-1])
