x, l = True, []

while x:
    x = int(input())
    if x:
        l.append(x)

m = 2 * max(l) + 1
a = [1 for _ in range(m + 1)]

for i in range(2, m):
    if a[i]:
        for j in range(2 * i, m + 1, i):
            a[j] = 0

for n in l:
    print(sum(a[i] for i in range(n + 1, 2 * n + 1) if i > 1))
