n, l = int(input()), lambda: sorted([*map(int, input().split())])
a, b = l()[::-1], l()
print(sum(a[i]*b[i] for i in range(n)))
