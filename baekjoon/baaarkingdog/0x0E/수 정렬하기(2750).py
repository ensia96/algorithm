l, c = lambda: map(int, input().split()), []
n, m = l()
a, b, i, j = [*l()], [*l()], 0, 0

while i < n and j < m:
    if j == m or a[i] <= b[j]:
        c += [a[i]]
        i += 1
    else:
        c += [b[j]]
        j += 1

print(c+a[i:]+b[j:])
