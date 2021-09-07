i, a, c = lambda: int(input()), 1, 0
n, m, d = i(), i(), [1, 1]
_ = [d.append((d[i-1])+d[i-2]) for i in range(2, n+1)]
for _ in [i() for _ in range(m)]:
    a, c = a * d[_-c-1], _
a *= d[n-c]
print(a)
